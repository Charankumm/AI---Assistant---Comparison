blocked_keywords = [
    "hack",
    "malware",
    "virus",
    "bomb",
    "steal password",
    "phishing"
]
def is_safe(user_input):
    user_input = user_input.lower()
    for word in blocked_keywords:
        if word in user_input:
            return False
    return True