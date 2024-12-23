# password_generator.py

import random
from datetime import datetime

# Character sets for password generation
char_sets = {
    "?l": "abcdefghijklmnopqrstuvwxyz",
    "?u": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "?d": "0123456789",
    "?s": "!@#$%^&*()",
}

# Function to generate a random password
def generate_password(length):
    try:
        if length < 1 or length > 25:
            raise ValueError("Password length must be between 1 and 25.")
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = "".join(random.choice(chars) for _ in range(length))
        return password
    except ValueError as e:
        return str(e)

# Function to evaluate password strength
def evaluate_strength(password):
    strength = "Weak"
    if len(password) >= 12 and any(c.islower() for c in password) and any(c.isupper() for c in password) and \
            any(c.isdigit() for c in password) and any(c in "!@#$%^&*()" for c in password):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"
    return strength

# Function to save passwords to a file
def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(f"{password} - Generated at {datetime.now()}\n")
    return "Password has been saved to passwords.txt"
