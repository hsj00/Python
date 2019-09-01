'''
class, __init__, __name__, __main__ 개념에 대해 추가 학습 필요
'''

# Q1 Calculator class

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCal(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCal()
cal.add(10)
cal.minus(7)

print(cal.value)

# Q2 MaxLimitCal

class MaxLimitCal(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCal()
cal.add(50)
cal.add(60)

print(cal.value)

# Q3
all(1, 2, abs(-3)-3) # False
chr(ord('a')) == 'a' # True

# Q4
## list: 반복 가능한 자료형을 입력받아 리스트로 만들어 돌려주는 함수
## filter: filter(함수, 함수에 들어갈 자료), 함수에서 반환값이 참인 것을 걸러내서 돌려준다
list(filter(lambda x : x > 0, [1, -2, 3, -5, 8, -3, 9, -10]))
## (lambda 인수 : 인수에 대한 조건, 처리할 자료)

# Q5 hex to dec
## hex: 정수를 입력받아 16진수로 반환
## int: 입력받은 자료를 정수로 반환 (str, float -> int), n진수 값을 10진수로 반환도 가능
# hex(234) to dec // '0xea'
int(hex(234), 16)
int('0xea', 16)

# Q6
## map: 함수에 자료들을 입력하여 수행한 결과들을 묶어서 반환
list(map(lambda x : x*3, [1, 2, 3, 4]))

# Q7 min/max

a = [-8, 2, 7, 5, -3, 5, 0, 1]

min(a) + max(a)

# Q8 round(a, b)

round(17/3, 4)

# Q9, sys.argv

""" ## 풀이 코드
import sys

numbers = sys.argv[1:]

result = 0
for number in numbers:
    result += int(number)
print(result)
 """

import sys
a = sys.argv # numbers = sys.argv[1:]
del a[0]

sum = 0
for i in range(0, len(a)): # i in numbers
    sum += int(a[i]) # int(i)
print(sum)

# Q10, os function
## windows

import os

os.chdir("d:/")
os.system("dir")
a = os.popen("dir")
print(a.read())

# Q11 glob function
## windows

import glob

a = glob.glob("d:/python_prac/*.py")
print(a)
print(len(a))


# Q12 time module
## YYYY/MM/DD hh:mm:ss

import time

""" # 풀이 코드
d = time.strftime("%Y%m%d %H:%M:%S")
print(d)
 """

## Sun Sep  1 19:05:52 2019
a = time.strftime('%c', time.localtime(time.time()))
print(a)


## Sun Sep  1 19:05:52 2019
b = time.asctime(time.localtime(time.time()))
print(b)

## 09/01/19 19:05:52
c = time.strftime('%x %X', time.localtime(time.time()))
print(c)


# Q13, random module
## lotto number extract

""" # 풀이 코드
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)
 """

import random

lotto = 0

if lotto != random.randint(1, 45):
    for i in range(6):
        lotto = random.randint(1, 45)
        print(lotto)
