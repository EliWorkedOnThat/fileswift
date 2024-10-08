# Welcome message
print("Welcome to the encryption program")
print()

# User input
message = input("What message would you like to encrypt: ")
shift = int(input("Enter the shift value (e.g., 3): "))

# Encryption
def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        # Encrypt letters only
        if char.isalpha():
            shift_amount = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_message += char  # Keep non-letter characters unchanged
    return encrypted_message

# Decryption
def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)  # Just reverse the shift for decryption

# Encrypt the message
encrypted_message = encrypt(message, shift)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted message: {decrypted_message}")
