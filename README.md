# Password Generator GUI

A simple and modern password generator with a graphical user interface (GUI) built using `customtkinter` and Python. The app allows users to generate secure passwords, evaluate their strength, and save them to a file. It supports a dark/light theme toggle and includes a progress bar for password generation.

## Features:
- Password generation with varying complexities: low, medium, high.
- Display password strength (Weak, Medium, Strong).
- Copy password to clipboard.
- Save password to a text file.
- Toggle between dark and light themes.
- Sleek UI with animation for the theme toggle.

---

## Files

### 1. `main.py`

**Overview**:
`main.py` is the core of the password generator application, providing the user interface (UI) using `customtkinter`. The app supports password generation, theme toggling, and password saving features.

#### Key Functions:

- **`generate_password_action(length_var, result_label, strength_label, progress_bar, complexity)`**: 
  Triggers password generation based on input length and complexity, and updates the UI with the generated password and strength.

- **`generate_password(length, complexity)`**:
  Generates a random password with the given length and complexity.

- **`evaluate_strength(password)`**:
  Evaluates and returns the strength of the password.

- **`copy_to_clipboard(app, result_label)`**:
  Copies the generated password to the system clipboard.

- **`toggle_theme()`**:
  Toggles between dark and light themes.

- **`main()`**:
  Initializes and runs the Tkinter app with all UI elements.

---

### 2. `password_generator.py`

**Overview**:
`password_generator.py` contains the logic for generating passwords, evaluating their strength, and saving them to a file. It defines functions for different levels of password complexity.

#### Key Functions:

- **`generate_password(length, complexity)`**:
  Generates a password of specified length and complexity. Complexity options:
  - `low`: Only lowercase letters.
  - `medium`: Lowercase letters, uppercase letters, and digits.
  - `high`: Lowercase letters, uppercase letters, digits, and punctuation.

- **`evaluate_strength(password)`**:
  Evaluates the password strength based on its length:
  - `Weak`: Passwords less than 8 characters.
  - `Medium`: Passwords between 8 and 12 characters.
  - `Strong`: Passwords 12 characters or more.

- **`save_password(password)`**:
  Saves the generated password to a file and returns a message indicating success.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Myasirjamil/password-generator.git
   cd password-generator
   python3 main.py 
