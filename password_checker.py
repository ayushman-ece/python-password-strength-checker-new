
import string


def check_password(password):
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Uppercase letter": any(c.isupper() for c in password),
        "Lowercase letter": any(c.islower() for c in password),
        "Number": any(c.isdigit() for c in password),
        "Special character": any(
            c in string.punctuation for c in password
        ),
    }

    score = sum(checks.values())

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "checks": checks,
    }
