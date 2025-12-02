"""
Exericse 1

Ask the user for their name and print a message:

Hello, <name>!
"""
import sys


def main():
    user_name = input("Enter your name: ")
    # handle missing name
    if user_name == "":
        print("No name found.")
        return 1
    elif not user_name.isalpha():
        print("Invalid name.")
        return 1
    # handle non-ascii name

    print(f"Hello {user_name}!")
    return 0 # OK


if __name__ == '__main__':
    sys.exit(main())