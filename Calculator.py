import re

def check_password_strength(password):

    if len(password)<8:
        return "week password : password must be at least 8 charecters long."
    if not any(char.isdigit() for char in password):
        return "week password : password must be maintain at least one number."
    if not any(char.isupper() for char in password):
        return "week password : password must be maintain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "week password : password must be maintain at one lowercase letter."
    if not re.search(r'[!@#$%^&*,.?":(){|<>]',password):
        return "Use other symbols to make more harder your password."
    return "Strong : your pasword is secure!"

def password_checker():

    print("Checking strength of your password...")

    while True:
        password = input("\nEnter your password (or type'exit' to quit):")

        if password.lower()=="exit":
            print("Thank you! we wre exiting you from here ")
            break
        result = check_password_strength(password)
        print(result)

if __name__ == "__main__":
    password_checker()
