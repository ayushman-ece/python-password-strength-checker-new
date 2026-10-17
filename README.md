# 🔐 Password Strength Checker

**A modular Python command-line tool that evaluates password composition and provides an easy-to-understand security checklist.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-111827)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-16A34A)

---

## 📌 Overview

The Password Strength Checker evaluates a password against five basic composition requirements: minimum length, uppercase letters, lowercase letters, numbers, and special characters.

It assigns a score out of five and classifies the result as Weak, Moderate, or Strong. The project demonstrates modular Python programming, string processing, Boolean conditions, and reusable functions.

> **Security note:** This is an educational rule-based checker. A strong score does not guarantee that a password is resistant to guessing, phishing, or data breaches.

## ✨ Features

- Evaluate password length
- Check for uppercase and lowercase letters
- Check for numeric digits
- Check for special characters
- Calculate a score out of five
- Classify passwords as Weak, Moderate, or Strong
- Display a checklist of passed and missing requirements
- Hide typed password input where terminal support allows
- Keep analysis logic separate from user interaction

## 🛠️ Tech Stack

- Python 3
- `string` standard-library module
- `getpass` for hidden terminal input
- Functions, dictionaries, loops, and Boolean expressions

No third-party packages or API keys are required.

## 📁 Project Structure

```text
python-password-strength-checker/
├── main.py
├── password_checker.py
└── README.md
```

- **`main.py`** handles user input and displays the results.
- **`password_checker.py`** evaluates password composition and returns the analysis.

## 🚀 Getting Started

### Prerequisites

Python 3.8 or newer.

### Installation

Clone the repository:

```bash
git clone https://github.com/ayushman-ece/python-password-strength-checker.git
```

Navigate to the project folder:

```bash
cd python-password-strength-checker
```

Run the application:

```bash
python main.py
```

## 💻 How It Works

The checker evaluates five requirements:

| Requirement | Rule |
|---|---|
| Length | At least 8 characters |
| Uppercase | Contains an uppercase letter |
| Lowercase | Contains a lowercase letter |
| Number | Contains a digit |
| Special character | Contains punctuation |

Each passed requirement adds one point.

| Score | Classification |
|---|---|
| 0–2 | Weak |
| 3–4 | Moderate |
| 5 | Strong |

These categories are simple educational classifications, not a formal security standard.

## 🧠 Concepts Learned

- Working with strings
- Using `any()` with generator expressions
- Evaluating Boolean conditions
- Counting passed checks
- Organizing code into separate modules
- Returning structured results using dictionaries
- Using `getpass` for terminal input

## 🔮 Future Improvements

- Estimate password entropy
- Check common-password lists locally
- Add a graphical user interface
- Provide more detailed password recommendations
- Add automated unit tests

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [@ayushman-ece](https://github.com/ayushman-ece)

---

*Built with Python to practise string processing, modular programming, and basic security concepts.*