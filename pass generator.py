import tkinter as tk
import string
import random

def generate_password(lenght=8):
    characters = string.ascii_letters+string.digits
    password = ''.join(random.choice(characters) for i in range(lenght))
    return password

def generate_and_show_password():
    password_length = int(entry.get())
    generated_password = generate_password(password_length)
    password_label.config(text="Generated Password: " + generated_password)

window = tk.Tk()
window.title("Key Generator")
window.geometry("350x235")
window.configure(bg="Grey")

label = tk.Label(window, text="Password Generator", font=("Helvetica",16), fg="purple",padx=10, pady=5)
label.pack(pady=15)

entry = tk.Entry(window,font=("Arial",14), fg="purple", bg="white",justify="center", width=20)
entry.pack(padx=5,pady=7)

generate_button = tk.Button(window, text="Generate", command=generate_and_show_password, 
                            font=("Arial", 12), fg="black", bg="lightgrey", activebackground="pink")
generate_button.pack(padx=9,pady=15)

password_label = tk.Label(window, text="", font=("Arial",14), fg="purple", bg="white" ,padx=10, pady=5)
password_label.pack(padx=15,pady=9)

window.mainloop()