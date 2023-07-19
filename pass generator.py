import string
import random

def generate_password(lenght=8):
    characters = string.ascii_letters+string.digits
    password = ''.join(random.choice(characters) for i in range(lenght))
    return password
if __name__== "__main__":
    password_lenght = int(input("Enter the lenght: "))
    generated_password = generate_password(password_lenght)
    print(generated_password)