import re

# Step 1: Define a function to check password strength
def check_password_strength(password):
    # Check if password meets required conditions
    length_error = len(password) < 8                     # Step 1a: Minimum 8 characters
    lowercase_error = re.search(r"[a-z]", password) is None  # Step 1b: At least one lowercase
    uppercase_error = re.search(r"[A-Z]", password) is None  # Step 1c: At least one uppercase
    digit_error = re.search(r"\d", password) is None         # Step 1d: At least one digit
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None  # Step 1e: At least one special char

    # Count how many requirements are missing
    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_error]
    score = 5 - sum(errors)  # Step 1f: Calculate strength score

    # Step 1g: Return strength as STRONG, MEDIUM, or WEAK
    if score == 5:
        return "STRONG"
    elif 3 <= score < 5:
        return "MEDIUM"
    else:
        return "WEAK"


# Step 2: Create main function to run tester
def main():
    print("\n🔐 Password Strength Tester 🔐")
    print("Enter 'quit' to exit\n")

    # Step 3: Take user input in a loop
    while True:
        password = input("Enter password: ")
        if password.lower() == "quit":    # Step 3a: Exit condition
            print("Exiting… Stay secure! 🔒")
            break

        # Step 4: Check password strength
        strength = check_password_strength(password)

        # Step 5: Print feedback
        if strength == "STRONG":
            print(f"\033[92mStrength: {strength} ✅\033[0m\n")  # Green for strong
        elif strength == "MEDIUM":
            print(f"\033[93mStrength: {strength} ⚠️\033[0m\n")  # Yellow for medium
        else:
            print(f"\033[91mStrength: {strength} ❌\033[0m\n")  # Red for weak


# Run the program
if __name__ == "__main__":
    main()
