# Q7 min/max

a = [-8, 2, 7, 5, -3, 5, 0, 1]

min(a)
max(a)

# Q8 round(a, b)

round(17/3, 4)

# Q9, sys.argv

import sys
a = sys.argv
del a[0]

sum = 0
for i in range(0, len(a)):
    sum += int(a[i])

print(sum)

# Q10, os function

import os

os.chdir("d:/")
os.system("dir")
a = os.popen("dir")
print(a.read())

# Q11 glob function

import glob

a = glob.glob("d:/python_prac/*.py")
print(a)
print(len(a))

