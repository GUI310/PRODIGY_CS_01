from caesar_cipher import encrypt, decrypt

def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        encrypted_text = encrypt(text, shift)
        with open(output_file, 'w') as f:
            f.write(encrypted_text)
        print(f"File encrypted successfully. Output saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")

def decrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        decrypted_text = decrypt(text, shift)
        with open(output_file, 'w') as f:
            f.write(decrypted_text)
        print(f"File decrypted successfully. Output saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
