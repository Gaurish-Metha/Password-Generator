import tkinter as tk
from tkinter import messagebox
import random
import string
import math
import pyperclip

# GOATED char set — no confusion chars, high entropy
upper = "ABCDEFGHJKLMNPQRSTUVWXYZ"
lower = "abcdefghijkmnopqrstuvwxyz"
digits = "23456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?~"
all_chars = upper + lower + digits + symbols
char_set_size = len(set(all_chars))  # ~85

# Calculate entropy
def calc_entropy(length):
    return round(length * math.log2(char_set_size), 2)

# Update entropy + slider label
def update_slider(val):
    val = int(val)
    entropy = calc_entropy(val)
    slider_value_label.config(text=f"{val} chars | Entropy: {entropy} bits")
    if entropy < 90:
        slider_value_label.config(fg="orange")
    else:
        slider_value_label.config(fg="lime")

# Generate password
def generate_password():
    length = slider.get()

    if length < 8:
        messagebox.showwarning("Too Short", "⚠️ Come on bro, minimum is 8 chars.")
        return

    # At least one of each type
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill remaining
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    final_password = ''.join(password)

    # Copy + display
    entropy = calc_entropy(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)

    status_label.config(text=f"✅ Copied to clipboard! Entropy: {entropy} bits",
                        fg="lime" if entropy >= 90 else "orange")

# ------------------ UI STARTS HERE ------------------

root = tk.Tk()
root.title("🧠 GOATED Password Generator 🧠")
root.geometry("600x420")
root.config(bg="#0d0d0d")  # dark mode vibes

font_title = ("Consolas", 18, "bold")
font_label = ("Consolas", 12)
font_status = ("Consolas", 11)

# Title
title = tk.Label(root, text="💻 GOATED PASSWORD GENERATOR 💻", fg="#00ffff", bg="#0d0d0d", font=font_title)
title.pack(pady=15)

# Slider title
slider_label = tk.Label(root, text="🛠️ Choose your password length:", bg="#0d0d0d", fg="white", font=font_label)
slider_label.pack()

# Slider
slider = tk.Scale(root, from_=8, to=32, orient="horizontal", length=350, showvalue=0,
                  command=update_slider, bg="#0d0d0d", fg="cyan", highlightbackground="#0d0d0d",
                  troughcolor="#333333", activebackground="#00ffff", sliderrelief="raised")
slider.set(16)
slider.pack(pady=10)

# Slider info
slider_value_label = tk.Label(root, text="", font=font_status, bg="#0d0d0d", fg="lime")
slider_value_label.pack()
update_slider(slider.get())

# Generate button
generate_btn = tk.Button(root, text="🎲 Generate Password", command=generate_password,
                         font=font_label, bg="#1a1a1a", fg="white", activebackground="#00ff99",
                         padx=20, pady=5, relief="ridge", cursor="hand2")
generate_btn.pack(pady=15)

# Password output
password_entry = tk.Entry(root, font=("Consolas", 14), width=35, justify="center",
                          bg="#191919", fg="lime", insertbackground="white", relief="sunken")
password_entry.pack(pady=10)

# Status
status_label = tk.Label(root, text="", font=font_status, bg="#0d0d0d", fg="lime")
status_label.pack()

# 🔒 Privacy notice
privacy_label = tk.Label(
    root,
    text="🔒 Note: Passwords are generated locally and never stored or sent anywhere.",
    font=("Consolas", 9),
    fg="#888",
    bg="#0d0d0d"
)
privacy_label.pack(pady=10)

# 👑 Footer credit
footer = tk.Label(
    root,
    text="🐐 Powered by ChatGPT x GaurishTheGoat",
    font=("Consolas", 9),
    fg="#555",
    bg="#0d0d0d"
)
footer.pack(side="bottom", pady=5)

root.mainloop()
