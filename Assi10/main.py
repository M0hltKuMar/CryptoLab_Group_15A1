import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare, binomtest

FILES = {
    "Linux /dev/urandom": "linux_urandom.bin",
    "OpenSSL": "openssl_random.bin",
    "Windows CNG": "windows_cng.bin"
}

for name, filename in FILES.items():

    print("\n==============================")
    print(name)
    print("==============================")

    with open(filename, "rb") as f:
        data = f.read()

    if len(data) < 1024 * 1024:
        raise ValueError(f"{filename} contains less than 1 MB")

    data = data[:1024 * 1024]

    # Convert bytes to NumPy array
    arr = np.frombuffer(data, dtype=np.uint8)

    # 1. Byte frequency distribution
    freq = np.bincount(arr, minlength=256)

    expected = len(arr) / 256

    chi_stat, chi_p = chisquare(freq)

    print("\nByte Frequency Analysis")
    print("Chi-square statistic:", chi_stat)
    print("P-value:", chi_p)

    plt.figure()
    plt.bar(range(256), freq)
    plt.title(name + " - Byte Frequency")
    plt.xlabel("Byte Value")
    plt.ylabel("Frequency")
    plt.show()

    # 2. Bit distribution
    bits = np.unpackbits(arr)

    ones = np.sum(bits)
    zeros = len(bits) - ones

    result = binomtest(ones, len(bits), 0.5)

    print("\nBit Distribution")
    print("Ones:", ones)
    print("Zeros:", zeros)
    print("One-bit proportion:", ones / len(bits))
    print("Binomial test p-value:", result.pvalue)

    plt.figure()
    plt.bar(["Zeros", "Ones"], [zeros, ones])
    plt.title(name + " - Bit Distribution")
    plt.show()

    # 3. Repeated patterns
    blocks = [
        data[i:i+16]
        for i in range(0, len(data)-15, 16)
    ]

    unique_blocks = len(set(blocks))
    repeated_blocks = len(blocks) - unique_blocks

    print("\nRepeated 16-byte Blocks")
    print("Total blocks:", len(blocks))
    print("Repeated blocks:", repeated_blocks)

    # Longest run of identical consecutive bytes
    max_run = 1
    current_run = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 1

    print("Longest identical-byte run:", max_run)

    # 4. Serial correlation
    correlation = np.corrcoef(
        arr[:-1].astype(float),
        arr[1:].astype(float)
    )[0, 1]

    print("\nSerial Correlation")
    print("Lag-1 correlation:", correlation)

    # 5. Runs test
    median = np.median(bits)
    binary = bits > median

    # 5. Correct Runs Test
    runs = 1 + np.sum(bits[1:] != bits[:-1])

    print("\nRuns Test")
    print("Number of runs:", runs)
