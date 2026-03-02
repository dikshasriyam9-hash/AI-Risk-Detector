from detectors.manipulation import detect_manipulation
from detectors.secrecy import detect_secrecy
from detectors.urgency import detect_urgency

def analyse(message):
    score = 0

    score += detect_manipulation(message)
    score += detect_secrecy(message)
    score += detect_urgency(message)

    if score == 0:
        return "Low Risk"
    elif score <= 2:
        return "Medium Risk"
    else:
        return "High Risk"

msg = input("Enter message: ")
print(analyse(msg))
