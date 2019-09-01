# Q13, random module
## lotto number extract
""" 
import random

lotto = 0

if lotto != random.randint(1, 45):
    for i in range(6):
        lotto = random.randint(1, 45)
        print(lotto)

 """


import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)
