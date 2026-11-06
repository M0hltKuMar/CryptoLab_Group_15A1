
import secrets
import time
import sympy

# Configuration
BITS = 512

BASES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71
]

ROUNDS = len(BASES)


# Miller-Rabin primality test
def miller_rabin(n, bases):

    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    # Express n-1 = 2^s * d
    d = n - 1
    s = 0

    while d % 2 == 0:
        s += 1
        d //= 2

    # Test each base
    for a in bases:

        a = a % n

        if a == 0 or a == 1:
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):

            x = pow(x, 2, n)

            if x == n - 1:
                break

        else:
            return False

    return True


# Generate a random 512-bit odd candidate
def generate_candidate():

    return secrets.randbits(BITS) | (1 << (BITS - 1)) | 1


# Main experiment
start_time = time.perf_counter()

candidates_tested = 0

while True:

    candidate = generate_candidate()
    candidates_tested += 1

    if miller_rabin(candidate, BASES):
        prime = candidate
        break

end_time = time.perf_counter()

execution_time = end_time - start_time


# Independent verification using SymPy
verified = sympy.isprime(prime)

# Display experimental results
print("\n----- EXPERIMENTAL RESULTS -----")

print("Assigned bit length:", BITS)
print("Generated prime:", prime)
print("Actual bit length:", prime.bit_length())
print("Candidates tested:", candidates_tested)
print("Miller-Rabin rounds:", ROUNDS)
print("Execution time:", execution_time, "seconds")

print("\n----- VERIFICATION -----")

print("Exact bit length:", prime.bit_length() == BITS)
print("Miller-Rabin result:", miller_rabin(prime, BASES))
print("SymPy independent verification:", verified)

print("\n----- BASE TESTING -----")

for base in BASES:
    print("Base", base, ":", miller_rabin(prime, [base]))
