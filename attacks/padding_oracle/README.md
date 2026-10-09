PADDING ORACLE ATTACK ON AES-CBC
================================

1. AIM
-----
Recover plaintext from AES-CBC encrypted data without knowing the AES key during the attack.

2. REQUIREMENTS
---------------
- Python 3
- cryptography library

Install the required library using:

pip install cryptography

3. HOW IT WORKS
---------------
1. Encrypt a message using AES-CBC.
2. Use a padding oracle to check whether the decrypted ciphertext has valid PKCS#7 padding.
3. Modify the previous ciphertext block.
4. Query the oracle and analyze its responses.
5. Recover plaintext bytes from right to left.
6. Recover the complete plaintext and count oracle queries.

4. IMPLEMENTATION
-----------------
The Python program performs the following tasks:

- Generates an AES key and initialization vector (IV) for the demonstration.
- Encrypts a sample plaintext using AES-CBC.
- Implements a padding oracle that returns True or False.
- Recovers plaintext bytes using oracle queries without accessing the key in the attack function.
- Displays the recovered plaintext and total number of oracle queries.

5. HOW TO RUN
-------------
Save the Python program as:

padding_oracle.py

Install the dependency:

pip install cryptography

Run the program:

python padding_oracle.py

6. EXPECTED OUTPUT
------------------
The program displays:

- Original ciphertext
- Initialization vector (IV)
- Recovered plaintext
- Total number of oracle queries
- Whether plaintext recovery was successful

The number of oracle queries may vary between runs.

7. SECURITY RECOMMENDATIONS
---------------------------
- Use authenticated encryption such as AES-GCM.
- Authenticate ciphertext before decrypting it in legacy CBC systems.
- Do not reveal distinguishable padding error messages.
- Use established cryptographic libraries.
- Avoid implementing cryptographic protocols from scratch.

8. CONCLUSION
-------------
A Padding Oracle Attack exploits information leaked by a system that reveals whether decrypted ciphertext has valid padding.

By modifying ciphertext and observing oracle responses, an attacker can potentially recover plaintext without knowing the AES key.

This attack exploits weaknesses in the system's error handling rather than breaking AES itself.

9. NOTE
-------
This project is intended for educational purposes and local testing.

The AES key is used only for encryption and the simulated padding oracle. The attack function does not receive or access the key.
