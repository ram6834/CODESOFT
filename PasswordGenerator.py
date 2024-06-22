import random

password_length = int(input("Enter the desired length of the password: "))

upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lower_letters = upper_letters.lower()

digits = '0123456789'

punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

characters = upper_letters+ lower_letters + digits + punctuation

password = ""
for i in range(password_length):
    password += random.choice(characters)

print("Generated Password: ", password)
