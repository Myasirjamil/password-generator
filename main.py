import customtkinter as ctk
from tkinter import messagebox
import random
import string

# Password Generation Function
def generate_password(length, complexity):
    """Generates a random password based on length and complexity."""
    if length < 1 or length > 25:
        return "Password length must be between 1 and 25."
    
    # Define complexity based on the option selected
    characters = string.ascii_lowercase  # Start with lowercase letters
    if complexity == "medium":
        characters += string.ascii_uppercase + string.digits  # Add uppercase and digits
    elif complexity == "high":
        characters += string.ascii_uppercase + string.digits + string.punctuation  # Add special characters
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Evaluate Password Strength
def evaluate_strength(password):
    """Evaluates the strength of the generated password."""
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

# Generate Password Action
def generate_password_action(length_var, result_label, strength_label, progress_bar, complexity):
    try:
        length = int(length_var.get())
        if length < 1 or length > 25:
            raise ValueError("Password length must be between 1 and 25.")
        
        # Update progress bar while password is being generated
        progress_bar.set(0.2)
        
        # Generate password based on length and complexity
        password = generate_password(length, complexity)
        result_label.configure(text=password)  # Display password

        # Evaluate password strength
        strength = evaluate_strength(password)
        strength_label.configure(text=f"Strength: {strength}")

        # Update progress bar after generation
        progress_bar.set(1.0)
        
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Copy Password to Clipboard
def copy_to_clipboard(app, result_label):
    app.clipboard_clear()
    app.clipboard_append(result_label.cget("text"))
    app.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Toggle Theme Function
def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
        app.configure(fg_color="white")
        result_label.configure(text_color="black", fg_color="lightgray")
        strength_label.configure(text_color="green")
        title_label.configure(text_color="black")
        length_label.configure(text_color="black")
        complexity_label.configure(text_color="black")
        theme_button.configure(fg_color="gray85")
        progress_bar.configure(fg_color="lightgray")
    else:
        ctk.set_appearance_mode("Dark")
        app.configure(fg_color="gray20")
        result_label.configure(text_color="lime", fg_color="black")
        strength_label.configure(text_color="red")
        title_label.configure(text_color="white")
        length_label.configure(text_color="white")
        complexity_label.configure(text_color="white")
        theme_button.configure(fg_color="gray40")
        progress_bar.configure(fg_color="gray40")

def main():
    global app, result_label, strength_label, theme_button, title_label, length_label, progress_bar, complexity_label
    
    app = ctk.CTk()
    app.geometry("600x750")
    app.title("Advanced Password Generator")
    app.configure(fg_color="gray20")
    
    ctk.set_appearance_mode("Dark")
    
    # Title
    title_label = ctk.CTkLabel(app, text="Password Generator", font=("Poppins", 24, "bold"), text_color="white")
    title_label.pack(pady=20)

    # Length Label and Entry
    length_label = ctk.CTkLabel(app, text="Password Length (1-25):", text_color="white")
    length_label.pack(pady=10)

    length_var = ctk.StringVar(value="12")
    length_entry = ctk.CTkEntry(app, textvariable=length_var, width=200, font=("Poppins", 14))
    length_entry.pack(pady=5)

    # Complexity Options
    complexity_label = ctk.CTkLabel(app, text="Password Complexity:", text_color="white")
    complexity_label.pack(pady=10)
    
    complexity_var = ctk.StringVar(value="medium")  # Complexity options: low, medium, high
    complexity_menu = ctk.CTkOptionMenu(app, variable=complexity_var, values=["low", "medium", "high"])
    complexity_menu.pack(pady=5)

    # Generate Password Button
    generate_button = ctk.CTkButton(app, text="Generate Random Password", font=("Poppins", 14),
                                    command=lambda: generate_password_action(length_var, result_label, strength_label, progress_bar, complexity_var.get()),
                                    width=250, corner_radius=20)
    generate_button.pack(pady=10)

    # Password Result Label
    result_label = ctk.CTkLabel(app, text="Generated password will appear here", font=("Poppins", 18),
                                fg_color="black", text_color="lime", corner_radius=8)
    result_label.pack(pady=10, ipadx=20, ipady=10)

    # Strength Label
    strength_label = ctk.CTkLabel(app, text="Strength: Weak", font=("Poppins", 14), text_color="red")
    strength_label.pack(pady=10)

    # Progress Bar for Password Generation
    progress_bar = ctk.CTkProgressBar(app, width=500, height=10, mode="determinate")
    progress_bar.pack(pady=10)
    
    # Copy Password Button
    copy_button = ctk.CTkButton(app, text="Copy Password", font=("Poppins", 14), command=lambda: copy_to_clipboard(app, result_label))
    copy_button.pack(pady=10)

    # Save Password Button
    save_button = ctk.CTkButton(app, text="Save Password to File", font=("Poppins", 14), command=lambda: save_password_action(result_label))
    save_button.pack(pady=10)

    # Circular Dark/Light Theme Toggle Button
    theme_button = ctk.CTkButton(app, text="☾", font=("Poppins", 18), width=50, height=50, corner_radius=25,
                                 command=toggle_theme, fg_color="gray40")
    theme_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)  # Top-right corner

    app.mainloop()

if __name__ == "__main__":
    main()
