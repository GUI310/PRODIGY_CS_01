import argparse
from caesar_cipher import encrypt, decrypt

def parse_args():
    parser = argparse.ArgumentParser(description='Caesar Cipher Encrypt/Decrypt')
    parser.add_argument('action', choices=['e', 'd'], help='Action to perform: encrypt or decrypt')
    parser.add_argument('message', help='The message to encrypt/decrypt')
    parser.add_argument('shift', type=int, help='The shift value (1-25)')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.action == 'e':
        encrypted = encrypt(args.message, args.shift)
        print(f"Encrypted: {encrypted}")
    else:
        decrypted = decrypt(args.message, args.shift)
        print(f"Decrypted: {decrypted}")

if __name__ == '__main__':
    main()
