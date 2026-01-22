from email import policy
from email.parser import BytesParser

def extract_email_body(file_path):
    with open(file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    try:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode(
                        part.get_content_charset() or "latin-1",
                        errors="ignore"
                    )
        else:
            return msg.get_payload(decode=True).decode(
                msg.get_content_charset() or "latin-1",
                errors="ignore"
            )
    except Exception:
        return ""
