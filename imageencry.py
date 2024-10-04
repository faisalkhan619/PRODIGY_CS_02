from cryptography.fernet import Fernet
import os

# Generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to 'key.key'.")

# Load the previously generated key
def load_key():
    if not os.path.exists('key.key'):
        print("Key not found. Please generate the key first.")
        return None
    with open('key.key', 'rb') as key_file:
        return key_file.read()

# Encrypt an image in place
def encrypt_image_in_place(image_path, key):
    if not os.path.exists(image_path):
        print(f"Image file {image_path} does not exist.")
        return
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(image_data)

    # Overwrite the original image file with the encrypted data
    with open(image_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"Image {image_path} has been encrypted in place.")

# Decrypt an image in place
def decrypt_image_in_place(image_path, key):
    if not os.path.exists(image_path):
        print(f"Encrypted file {image_path} does not exist.")
        return

    with open(image_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)

    # Overwrite the original file with the decrypted data
    with open(image_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Encrypted image {image_path} has been decrypted in place.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Generate encryption key")
        print("2. Encrypt an image (in place)")
        print("3. Decrypt an image (in place)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            generate_key()

        elif choice == '2':
            key = load_key()
            if key:
                image_path = input("Enter the path of the image to encrypt: ")
                encrypt_image_in_place(image_path, key)

        elif choice == '3':
            key = load_key()
            if key:
                image_path = input("Enter the path of the image to decrypt: ")
                decrypt_image_in_place(image_path, key)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
