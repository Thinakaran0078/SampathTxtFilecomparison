from random import randint
import hashlib

#r = random.randint(1, 1000)
r = 'Geeks for Geeks'
for num in range(1, 100):
    txt = r + str(num)
    res = hashlib.sha256(txt.encode())
    result = res.hexdigest()
    output = str(result) + '~'
    with open('randomdata.txt', 'a') as text:
        text.writelines(output)
        text.write("\n")


