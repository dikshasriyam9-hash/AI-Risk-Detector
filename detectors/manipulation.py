manipulation_phrases = [
    "if you loved me",
    "prove your love",
    "you don't trust me",
    "you are overthinking",
    "only you understand me"
]

def detect_manipulation(message):
    score = 0
    message = message.lower()

    for phrase in manipulation_phrases:
        if phrase in message:
            score += 1

    return score
