
from getpass import getpass
from password_checker import check_password


def main():
    print("=" * 35)
    print("    PASSWORD STRENGTH CHECKER")
    print("=" * 35)
    print("Your password is checked locally.")
    print("Input is hidden while typing.\n")

    password = getpass("Enter a password to check: ")

    if not password:
        print("Password cannot be empty.")
        return

    result = check_password(password)

    print(f"\nStrength: {result['strength']}")
    print(f"Score: {result['score']}/5")

    print("\n--- Security Checklist ---")
    for requirement, passed in result["checks"].items():
        status = "PASS" if passed else "MISSING"
        print(f"[{status}] {requirement}")

    if result["strength"] != "Strong":
        print("\nTip: Meet the missing requirements.")
    else:
        print("\nAll five checks passed!")

    print("\nNote: This is a basic rule-based check,")
    print("not a guarantee against password attacks.")


if __name__ == "__main__":
    main()
