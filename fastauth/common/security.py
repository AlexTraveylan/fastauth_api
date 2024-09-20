from cryptography.fernet import Fernet

if __name__ == "__main__":
    # Generate a key
    key = Fernet.generate_key()
    print(key)
