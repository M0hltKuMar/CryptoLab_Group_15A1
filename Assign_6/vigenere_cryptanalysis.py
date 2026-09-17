
from collections import Counter, defaultdict
from math import gcd
from functools import reduce
import string

ALPHABET = string.ascii_uppercase

# Approximate English letter frequencies
ENGLISH_FREQ = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
    0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
    0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
    0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
    0.02758, 0.00978, 0.02360, 0.00150, 0.01974,
    0.00074
]


def clean_ciphertext(text):
    """Keep only uppercase English letters."""
    return ''.join(
        ch for ch in text.upper() if ch in ALPHABET
    )


def find_repeated_patterns(ciphertext, min_len=3):
    """Find repeated sequences and their positions."""
    patterns = defaultdict(list)

    for size in range(min_len, 6):
        for i in range(len(ciphertext) - size + 1):
            pattern = ciphertext[i:i + size]
            patterns[pattern].append(i)

    return {
        pattern: positions
        for pattern, positions in patterns.items()
        if len(positions) > 1
    }


def calculate_distances(patterns):
    """Calculate distances between repeated occurrences."""
    distances = []

    for positions in patterns.values():
        for i in range(len(positions) - 1):
            distances.append(
                positions[i + 1] - positions[i]
            )

    return distances


def find_factors(distances):
    """Count factors of repeated-pattern distances."""
    factors = Counter()

    for distance in distances:
        for factor in range(2, min(distance, 30) + 1):
            if distance % factor == 0:
                factors[factor] += 1

    return factors


def kasiski_analysis(ciphertext):
    """Suggest likely key lengths using Kasiski."""
    patterns = find_repeated_patterns(ciphertext)
    distances = calculate_distances(patterns)
    factors = find_factors(distances)

    return factors.most_common(10)


def calculate_ic(text):
    """Calculate Index of Coincidence."""
    n = len(text)

    if n < 2:
        return 0

    counts = Counter(text)

    numerator = sum(
        count * (count - 1)
        for count in counts.values()
    )

    return numerator / (n * (n - 1))


def split_into_groups(ciphertext, key_length):
    """Split letters by their key position."""
    return [
        ciphertext[i::key_length]
        for i in range(key_length)
    ]


def frequency_analysis(group):
    """Return A-Z letter frequencies."""
    counts = Counter(group)
    return {
        letter: counts.get(letter, 0)
        for letter in ALPHABET
    }


def find_shift(group):
    """Estimate Caesar shift using chi-square."""
    best_shift = 0
    best_score = float("inf")
    n = len(group)

    if n == 0:
        return 0

    for shift in range(26):
        decrypted = ''.join(
            ALPHABET[(ALPHABET.index(ch) - shift) % 26]
            for ch in group
        )

        counts = Counter(decrypted)
        score = 0

        for i, letter in enumerate(ALPHABET):
            expected = ENGLISH_FREQ[i] * n
            observed = counts.get(letter, 0)

            if expected:
                score += (
                    (observed - expected) ** 2 / expected
                )

        if score < best_score:
            best_score = score
            best_shift = shift

    return best_shift


def find_key(groups):
    """Convert estimated shifts into key letters."""
    return ''.join(
        ALPHABET[find_shift(group)]
        for group in groups
    )


def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using a Vigenere key."""
    key = clean_ciphertext(key)
    result = []

    for i, ch in enumerate(ciphertext):
        c = ALPHABET.index(ch)
        k = ALPHABET.index(key[i % len(key)])

        result.append(ALPHABET[(c - k) % 26])

    return ''.join(result)


def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using a Vigenere key."""
    plaintext = clean_ciphertext(plaintext)
    key = clean_ciphertext(key)
    result = []

    for i, ch in enumerate(plaintext):
        p = ALPHABET.index(ch)
        k = ALPHABET.index(key[i % len(key)])

        result.append(ALPHABET[(p + k) % 26])

    return ''.join(result)


def verify(original, encrypted):
    """Check whether ciphertexts match."""
    return clean_ciphertext(original) == clean_ciphertext(encrypted)


def estimate_key_length(ciphertext):
    """Combine Kasiski factors and average IC."""
    kasiski = kasiski_analysis(ciphertext)
    candidates = {length for length, _ in kasiski}

    # Include candidates even if Kasiski finds few repeats.
    candidates.update(range(2, 21))

    def average_ic(length):
        groups = split_into_groups(ciphertext, length)
        values = [calculate_ic(g) for g in groups if len(g) > 1]
        return sum(values) / len(values) if values else 0

    # English text encrypted by Vigenere often has IC
    # around 0.06 for correctly separated groups.
    ranked = sorted(
        candidates,
        key=lambda length: abs(average_ic(length) - 0.066),
    )

    return ranked[0]


def main():
    print("VIGENERE CIPHER CRYPTANALYSIS")
    print("1. Odd group number")
    print("2. Even group number")

    choice = input("Choose ciphertext (1 or 2): ")

    if choice == "1":
        ciphertext = """
        DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA
        MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV
        GQSOH QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV
        POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM
        JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE
        OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM
        OECBX SESCI YGUFP KVILL TWDKS ZODFW FWEAA PQTFS
        TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU
        KWTAM ZJMLS EVJQT GLAWV OVVXH KWQIL IEUYS ZWXAH
        HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF
        """
    else:
        ciphertext = """
        QRBAI UWYOK ILBRZ XTUWL EGXSN VDXWR XMHXY FCGMW
        WWSME LSXUZ MKMFS BNZIF YEIEG RFZRX WKUFA XQEDX
        DTTHY NTBRJ LHTAI KOCZX QHBND ZIGZG PXARJ EDYSJ
        NUMKI FLBTN HWISW NVLFM EGXAI AAWSL FMHXR SGRIG
        HEQTU MLGLV BRSIL AEZSG XCMHT OWHFM LWMRK HPRFB
        ELWGF RUGPB HNBEM KBNVW HHUEA KILBN BMLHK XUGML
        YQKHP RFBEL EJYNV WSIJB GAXGO TPMXR TXFKI WUALB
        RGWIE GHWHG AMEWW LTAEL NUMRE UWTBL SDPRL YVRET
        LEEDF ROBEQ UXTHX ZYOZB XLKAC KSOHN VWXKS MAEPH
        IYQMM FSECH RFYPB BSQTX TPIWH GPXQD FWTAI KNNBX
        SIYKE TXTLV BTMQA LAGHG OTPMX RTXTH XSFYG WMVKH
        LOIVU ALMLD LTSYV WYNVW MQVXP XRVYA BLXDL XSMLW
        SUIOI IMELI SOYEB HPHNR WTVUI AKEYG WIETG WWBVM
        VDUMA EPAUA KXWHK MAUPA MUKHQ PWKCX EFXGW WSDDE
        OMLWL NKMWD FWTAM FAFEA MFZBN WIHYA LXRWK MAMIK
        GNGHJ UAZHM HGUAL YSULA ELYHJ BZMSI LAILH WWYIK
        EWAHN PMLBN NBVPJ XLBEF WRWGX KWIRH XWWGQ HRRXW
        IOMFY CZHZL VXNVI OYZCM YDDEY IPWXT MMSHS VHHXZ
        YEWNV OAOEL SMLSW KXXFX STRVI HZLEF JXDAS FIE
        """

    ciphertext = clean_ciphertext(ciphertext)

    print("\nCiphertext length:", len(ciphertext))

    print("\nKasiski candidate lengths:")
    print(kasiski_analysis(ciphertext))

    key_length = estimate_key_length(ciphertext)
    print("\nEstimated key length:", key_length)

    groups = split_into_groups(ciphertext, key_length)

    print("\nFrequency tables:")
    for i, group in enumerate(groups):
        print(f"\nGroup {i + 1}:")
        print(frequency_analysis(group))

    key = find_key(groups)
    print("\nProbable key:", key)

    plaintext = vigenere_decrypt(ciphertext, key)
    print("\nRecovered plaintext:")
    print(plaintext)

    encrypted = vigenere_encrypt(plaintext, key)

    print("\nVerification:", verify(ciphertext, encrypted))


if __name__ == "__main__":
    main()
