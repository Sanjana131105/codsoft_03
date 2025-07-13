import random
import string
def generate_password():
    print("Welcome to Password Generator!")
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be a positive number")
            return
        letters = string.ascii_letters  
        digits = string.digits          
        symbols = string.punctuation    
        all_chars = letters + digits + symbols
        password = ''.join(random.choice(all_chars) for _ in range(length))
        print(f"\nYour generated password is: {password}")
    except ValueError:
        print("Please enter a valid number.")
generate_password()
