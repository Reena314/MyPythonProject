import random
import string

def generate_password():
    print("\n===== PASSWORD GENERATOR =====")

    length = int(input("Enter password length: "))

    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Build password by randomly selecting characters
    password = "".join(random.choice(characters) for _ in range(length))   #The underscore (_) is used as a placeholder for the variable name because we don’t need to use the loop index value, just the repetition of the loop itself.

    print("Generated Password:", password)


# Run the password generator
generate_password()

