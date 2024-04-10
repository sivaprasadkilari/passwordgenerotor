import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_simple(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_medium(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_complex(length):
    characters = string.ascii_letters + string.digits + string.punctuation + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        print("Password Complexity Options:")
        print("1. Simple (Only letters and digits)")
        print("2. Medium (Letters, digits, and punctuation)")
        print("3. Complex (Letters, digits, punctuation, and special characters)")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '4':
            print("Exiting the program.")
            break

        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            continue

        switch = {
            '1': generate_password_simple,
            '2': generate_password_medium,
            '3': generate_password_complex,
        }

        if choice in switch:
            password = switch[choice](length)
            print("Generated Password:", password)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
