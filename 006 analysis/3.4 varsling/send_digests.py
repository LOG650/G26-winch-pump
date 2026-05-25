"""Sender ferdig genererte digester via Gmail SMTP (demo-modus).

Alle e-poster omdirigeres til TEST_RECIPIENT, men originaladressene
beholdes synlige i brødteksten for å vise hvem digesten egentlig
skulle gått til i produksjon.

Kjor (PowerShell):
    $env:GMAIL_APP_PASSWORD = "abcdefghijklmnop"
    uv run python "3.4 varsling/send_digests.py"
"""
import os
import re
import smtplib
import sys
from email.message import EmailMessage
from pathlib import Path

SENDER = "tordalinho@gmail.com"
TEST_RECIPIENT = "tordalinho@gmail.com"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

SCRIPT_DIR = Path(__file__).resolve().parent
DIGEST_DIR = SCRIPT_DIR / "digests"


def parse_digest(text: str) -> tuple[dict[str, str], str]:
    headers: dict[str, str] = {}
    body_lines: list[str] = []
    in_body = False
    for line in text.splitlines():
        if not in_body:
            if line.strip() == "":
                in_body = True
                continue
            match = re.match(r"^(To|Cc|Subject):\s*(.+)$", line)
            if match:
                headers[match.group(1)] = match.group(2).strip()
                continue
            in_body = True
        body_lines.append(line)
    return headers, "\n".join(body_lines)


def build_message(headers: dict[str, str], body: str, snapshot: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = SENDER
    msg["To"] = TEST_RECIPIENT
    msg["Subject"] = f"[DEMO] {headers['Subject']}"
    intro = (
        f"[Demo-utsending fra G26 WinchPump-varslingssystemet, snapshot {snapshot}.\n"
        f" Original To: {headers['To']}\n"
        f" Original Cc: {headers.get('Cc', '-')}\n"
        f" Begge omdirigert til {TEST_RECIPIENT} for demonstrasjon.]\n\n"
    )
    msg.set_content(intro + body)
    return msg


def main() -> int:
    password = os.environ.get("GMAIL_APP_PASSWORD")
    if not password:
        print("FEIL: GMAIL_APP_PASSWORD er ikke satt.", file=sys.stderr)
        print("Sett den i PowerShell med:", file=sys.stderr)
        print('  $env:GMAIL_APP_PASSWORD = "<din 16-tegns kode uten mellomrom>"', file=sys.stderr)
        return 1

    digest_files = sorted(DIGEST_DIR.glob("digest_*.txt"))
    if not digest_files:
        print(f"FEIL: ingen digest-filer i {DIGEST_DIR}", file=sys.stderr)
        return 1

    latest_date = max(p.name.split("_")[1] for p in digest_files)
    todays = [p for p in digest_files if p.name.split("_")[1] == latest_date]
    print(f"Snapshot: {latest_date}")
    print(f"Sender {len(todays)} digester -> {TEST_RECIPIENT}\n")

    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.login(SENDER, password.replace(" ", ""))
            for path in todays:
                text = path.read_text(encoding="utf-8")
                headers, body = parse_digest(text)
                msg = build_message(headers, body, latest_date)
                smtp.send_message(msg)
                print(f"  sendt: {path.name}")
                print(f"         (skulle gått til: {headers['To']})")
    except smtplib.SMTPAuthenticationError as e:
        print(f"\nFEIL: Gmail avviste innlogging. Sjekk at:", file=sys.stderr)
        print(f"  1. 2-faktor er aktivert paa {SENDER}", file=sys.stderr)
        print(f"  2. App Password er kopiert riktig (16 tegn, uten mellomrom)", file=sys.stderr)
        print(f"  3. App Password er ikke utlopt eller slettet i Google-kontoen", file=sys.stderr)
        print(f"\nGmail-svar: {e}", file=sys.stderr)
        return 2

    print(f"\nFerdig. Sjekk innboksen paa {TEST_RECIPIENT}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
