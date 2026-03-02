urgency_words = [
    "decide now",
    "don't wait",
    "hurry",
    "urgent",
    "quickly"
]

def detect_urgency(message):
    score = 0
    message = message.lower()

    for word in urgency_words:
        if word in message:
            score += 1

    return score
