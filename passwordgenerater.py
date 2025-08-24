import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- Password Generator ----------------
def generate_password():
    try:
        length = int(length_entry.get())
        rotation = int(rotation_entry.get())

        if length <= 0:
            messagebox.showwarning("Invalid", "Password length must be greater than 0")
            return

        # Characters pool
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        password = "".join(random.choice(chars) for _ in range(length))

        # Apply rotation like electric meter (wrap around)
        rotated_password = ""
        for ch in password:
            if ch.isdigit():
                rotated_password += str((int(ch) + rotation) % 10)
            elif ch.islower():
                rotated_password += chr((ord(ch) - ord('a') + rotation) % 26 + ord('a'))
            elif ch.isupper():
                rotated_password += chr((ord(ch) - ord('A') + rotation) % 26 + ord('A'))
            else:
                rotated_password += ch  # keep special chars unchanged

        password_var.set(rotated_password)

    except ValueError:
        messagebox.showwarning("Invalid", "Please enter valid numbers for length and rotation")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("🔐 Password Generator (Meter Style)")
root.geometry("400x300")
root.config(bg="lightblue")

# Labels & Entries
tk.Label(root, text="Password Length:", font=("Arial", 12), bg="lightblue").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

tk.Label(root, text="Rotation Number (Meter Shift):", font=("Arial", 12), bg="lightblue").pack(pady=5)
rotation_entry = tk.Entry(root, font=("Arial", 12))
rotation_entry.pack(pady=5)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="lightgreen", font=("Arial", 12))
generate_btn.pack(pady=10)

# Display Password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=30, state="readonly").pack(pady=10)

root.mainloop()
