import random
import string

sequence=(input("enter the length of the password you want to generate:"))
pool_of_characters=string.ascii_letters+"0123456789!@#%^&"

password="".join(random.choice(pool_of_characters) for _ in range(int(sequence)))
print(f"{password}")