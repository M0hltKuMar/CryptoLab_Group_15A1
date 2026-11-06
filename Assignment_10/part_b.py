
import random
import time


# Generate a 16-byte reset token using MT19937
def generate_token(timestamp):
    generator = random.Random(timestamp)

    token = bytes(
        generator.getrandbits(8) for _ in range(16)
    )

    return token


# Predict the timestamp by testing candidate seeds
def predict_timestamp(observed_token, start_time, end_time):
    tested = 0

    for timestamp in range(start_time, end_time + 1):
        tested += 1

        candidate_token = generate_token(timestamp)

        if candidate_token == observed_token:
            return timestamp, tested

    return None, tested


# Main program
def main():
    print("===== PART B: PREDICTABLE RESET TOKEN =====")

    # Record current Unix timestamp
    timestamp = int(time.time())

    # Generate reset token
    token = generate_token(timestamp)

    print("\n1. Token Generation")
    print("Original Timestamp:", timestamp)
    print("Generated Token (Hex):", token.hex())

    # Define attack search interval
    start_time = timestamp - 300
    end_time = timestamp + 300

    print("\n2. Attacker Search")
    print("Search Start:", start_time)
    print("Search End:", end_time)
    print("Search Interval: T-300 to T+300")

    # Predict timestamp
    recovered_timestamp, tested = predict_timestamp(
        token, start_time, end_time
    )

    print("\n3. Prediction Results")
    print("Total Timestamps Tested:", tested)

    if recovered_timestamp is not None:
        print("Recovered Timestamp:", recovered_timestamp)

        # Verify recovered timestamp
        recovered_token = generate_token(recovered_timestamp)

        print("\n4. Verification")
        print("Timestamp Correct:", recovered_timestamp == timestamp)
        print("Regenerated Token:", recovered_token.hex())
        print("Token Match:", recovered_token == token)

    else:
        print("No matching timestamp found.")


if __name__ == "__main__":
    main()
