from utils.logger import write_log
from analysis.file_analysis import analyze_file
def display_menu():
    print("\n========== CryptoLabX ==========")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")
    print("================================")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            write_log("Encrypt")
            print("\n[Encrypt] Coming Soon...")

        elif choice == "2":
            write_log("Decrypt")
            print("\n[Decrypt] Coming Soon...")

        elif choice == "3":
            write_log("Attack")
            print("\n[Attack] Coming Soon...")

        elif choice == "4":
            write_log("Analyze")
            analyze_file("datasets/sample1.txt")

        elif choice == "5":
            write_log("Exit")
            print("\nThank you for using CryptoLabX.")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()