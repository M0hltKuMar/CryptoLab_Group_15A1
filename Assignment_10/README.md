
# Cryptography Lab Assignment 10

## Title
MT19937 Stream Cipher and Predictable Token Attack

## Objective
To understand why statistical pseudorandom number generators are unsuitable for cryptographic applications by implementing a toy stream cipher, recovering a weak seed, and analyzing predictable reset tokens.

## Part A - MT19937 Stream Cipher
- Implemented stream cipher using MT19937.
- Used XOR for encryption and decryption.
- Generated plaintext containing 14 consecutive A characters.
- Used a randomly selected 16-bit seed.
- Brute-forced all 65,536 possible seeds.
- Recovered the matching seed and plaintext.

## Part B - Predictable Password Reset Tokens
- Generated a 16-byte token using MT19937.
- Used the current Unix timestamp as the seed.
- Tested timestamps within T-300 to T+300 seconds.
- Recovered the matching timestamp.
- Verified the regenerated token.

## Technologies Used
- Python 3
- random module
- secrets module
- time module
- MT19937 PRNG

## Files
- part_a.py: Stream cipher and seed recovery.
- part_b.py: Reset token generation and prediction.
- outputs/: Program execution results.

## Security Observation
MT19937 is designed for statistical randomness, not cryptographic security. Predictable seeds and known plaintext can make systems using it vulnerable to attacks.

## Author
Mohit & Aryan
