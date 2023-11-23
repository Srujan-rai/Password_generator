import random
import string

lowercase = string.ascii_lowercase
# print(lowercase)
uppercase = string.ascii_uppercase
digit = string.digits
specialCharacters = string.punctuation


length = int(input("Enter the length of the password: "))

all = lowercase + uppercase + digit + specialCharacters

# print(all)

password = ''.join(random.sample(all, length))

print(password)