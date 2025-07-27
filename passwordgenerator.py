import random
import string
print("\t PASSWORD GENERATOR")
length=int(input("enter length of the password:"))
character=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password+=random.choice(character)
print("YOUR PASSWORD:",password)
