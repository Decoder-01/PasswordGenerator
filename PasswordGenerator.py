import io
import random
import json

name= input("Enter your Username: ")
file = open("/home/dec001/Desktop/templates.txt", "a")
password=[]
passkey = ""


numeric = range(0, 9)
sym = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+"]
alphabets = []
# small letters
for i in range(97, 123):
    alphabets.append(chr(i))
# capital letters
for i in range(65, 90):
    alphabets.append(chr(i))
# Mixer
sym.extend(numeric)
sym.extend(alphabets)
for i in range(15):
    password.append( random.choice(sym))
for i in password:
    passkey=passkey+str(i)
print("Your password is: ",*password,sep="")

Data = {name:passkey}
result ="\n".join(f"{key}:{value}" for key,value in Data.items())
file.write("\n"+result)
print(result)
