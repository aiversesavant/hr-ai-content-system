import re


def redact_pii(text):
    text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED_SSN]", text)
    text = re.sub(r"\bSSN\b", "[REDACTED]", text)
    text = re.sub(r"\bsalary\b", "[REDACTED]", text)
    return text


def apply_rbac(results, role="employee"):
    filtered = []

    for r in results:
        text = r["text"]

        if role == "employee":
            text = redact_pii(text)

        filtered.append({
            "score": r["score"],
            "text": text,
            "metadata": r["metadata"]
        })

    return filtered