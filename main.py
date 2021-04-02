import random

# Enter the password length
PasswordLength = int(input("Enter the length of password\n"))

# Letters for the password
Letters = "zxcvbnmasdfghjklqwertyuiop0123456789*-+!@#$%^&*_-=/ZXCVBNMASDFGHJKLQWERTYUIOP"

# Join the Letters and the password length with random choices
ThePassword = "".join(random.sample(Letters, PasswordLength))
print(ThePassword)
