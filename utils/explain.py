suspicious_keywords = [
    "urgent",
    "verify",
    "account",
    "password",
    "login",
    "click",
    "bank",
    "security",
    "suspended",
    "confirm",
    "update",
    "payment",
    "limited",
    "immediately",
    "winner"
]

def detect_keywords(text):

    found = []

    text = text.lower()

    for keyword in suspicious_keywords:
        if keyword in text:
            found.append(keyword)

    return found