secrecy_words = [
    "secret",
    "don't tell",
    "our secret",
    "keep this private",
    "no one should know"
]

def detect_secrecy(message):
    score = 0
    message = message.lower()

    for word in secrecy_words:
        if word in message:
            score += 1

    return score
