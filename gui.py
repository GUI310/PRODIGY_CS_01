import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def encrypt_message():
    text = entry_message.get()
    shift = int(entry_shift.get())
    if text:
        encrypted = encrypt(text, shift)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, encrypted)
    else:
        messagebox.showwarning("Input Error", "Please enter a message to encrypt.")

def decrypt_message():
    text = entry_message.get()
    shift = int(entry_shift.get())
    if text:
        decrypted = decrypt(text, shift)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, decrypted)
    else:
        messagebox.showwarning("Input Error", "Please enter a message to decrypt.")

def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_val = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_val + shift) % 26 + shift_val)
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift_val = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_val - shift) % 26 + shift_val)
        else:
            decrypted += char
    return decrypted


window = tk.Tk()
window.title("Caesar Cipher - Encrypt/Decrypt")
window.geometry("600x500")
window.config(bg="#E0F7FA")  


style = ttk.Style()
style.configure("TButton",
                font=("Arial", 16, "bold"),
                background="#FF6347",
                foreground="white",
                padding=15,
                relief="flat")

style.map("TButton",
          background=[('active', '#FF4500')],  
          foreground=[('active', 'white')])

style.configure("TEntry", font=("Arial", 14), padding=5)


header_label = tk.Label(window, text="Caesar Cipher", font=("Arial", 30, "bold"), fg="#FF6347", bg="#E0F7FA")
header_label.pack(pady=30)


frame_message = tk.Frame(window, bg="#E0F7FA")
frame_message.pack(pady=20)

label_message = tk.Label(frame_message, text="Enter Text:", font=("Arial", 16, "bold"), bg="#E0F7FA")
label_message.grid(row=0, column=0, padx=10)
entry_message = ttk.Entry(frame_message, width=40, font=("Arial", 14))
entry_message.grid(row=0, column=1)


frame_shift = tk.Frame(window, bg="#E0F7FA")
frame_shift.pack(pady=20)

label_shift = tk.Label(frame_shift, text="Shift Value:", font=("Arial", 16, "bold"), bg="#E0F7FA")
label_shift.grid(row=0, column=0, padx=10)
entry_shift = ttk.Entry(frame_shift, width=10, font=("Arial", 14))
entry_shift.grid(row=0, column=1)


frame_buttons = tk.Frame(window, bg="#E0F7FA")
frame_buttons.pack(pady=30)

encrypt_button = ttk.Button(frame_buttons, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=0, column=0, padx=30)

decrypt_button = ttk.Button(frame_buttons, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=0, column=1, padx=30)


frame_result = tk.Frame(window, bg="#E0F7FA")
frame_result.pack(pady=20)

label_result = tk.Label(frame_result, text="Result:", font=("Arial", 16, "bold"), bg="#E0F7FA")
label_result.grid(row=0, column=0, padx=10)
entry_result = ttk.Entry(frame_result, width=40, font=("Arial", 14))
entry_result.grid(row=0, column=1)


window.mainloop()
