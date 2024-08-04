import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
