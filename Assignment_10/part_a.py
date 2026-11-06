
import random
import secrets
import string


# Function to generate keystream and encrypt/decrypt data
def stream_cipher(data, seed):
    generator = random.Random(seed)
    result = bytearray()

    for byte in data:
        key_byte = generator.getrandbits(8)
        result.append(byte ^ key_byte)

    return bytes(result)


# Generate random plaintext
def generate_plaintext():
    prefix_length = secrets.randbelow(16) + 5

    characters = string.ascii_letters + string.digits + string.punctuation
    prefix = ''.join(secrets.choice(characters) for _ in range(prefix_length))

    plaintext = prefix + "A" * 14
    return plaintext.encode()


# Brute-force all possible 16-bit seeds
def recover_seed(ciphertext):
    known_text = b"A" * 14

    for seed in range(65536):
        decrypted = stream_cipher(ciphertext, seed)

        if known_text in decrypted:
            return seed, decrypted

    return None, None


# Main program
def main():
    print("===== PART A: MT19937 STREAM CIPHER =====")

    # Test encryption and decryption
    test_message = b"Hello Cryptography"
    test_seed = 12345

    encrypted = stream_cipher(test_message, test_seed)
    decrypted = stream_cipher(encrypted, test_seed)

    print("\n1. Encryption and Decryption Test")
    print("Original Message:", test_message.decode())
    print("Encrypted (Hex):", encrypted.hex())
    print("Decrypted Message:", decrypted.decode())
    print("Test Successful:", decrypted == test_message)

    # Generate random plaintext and 16-bit seed
    plaintext = generate_plaintext()
    actual_seed = secrets.randbelow(65536)

    ciphertext = stream_cipher(plaintext, actual_seed)

    print("\n2. Generated Plaintext and Ciphertext")
    print("Plaintext:", plaintext.decode())
    print("Actual Seed:", actual_seed)
    print("Ciphertext (Hex):", ciphertext.hex())

    # Recover the seed
    print("\n3. Brute Force Seed Recovery")
    print("Searching all 65,536 possible seeds...")

    recovered_seed, recovered_plaintext = recover_seed(ciphertext)

    if recovered_seed is not None:
        print("Recovered Seed:", recovered_seed)
        print("Recovered Plaintext:", recovered_plaintext.decode())

        # Verify recovered result
        print("\n4. Verification")
        print("Seed Correct:", recovered_seed == actual_seed)
        print("Plaintext Correct:", recovered_plaintext == plaintext)
        print("Known 14 A's Found:", b"A" * 14 in recovered_plaintext)
    else:
        print("No matching seed found.")


if __name__ == "__main__":
    main()
