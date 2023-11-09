import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
    characters = ''
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Please specify at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage 

password_length = int(input("State Password length : "))
x = password_length
password = generate_password(password_length, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True)
print("Generated password:", password)
