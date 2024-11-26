def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Program")
    action = input("Would you like to encrypt or decrypt? (E/D): ").lower()
    
    if action not in ['e', 'd']:
        print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    if action == 'e':
        result = encrypt(text, shift)
        print(f"Encrypted message: {result}")
    elif action == 'd':
        result = decrypt(text, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
