# 001
import math
print(sum(x for x in range(1000) if x % 3==0 or x % 5==0))

import re

p = re.compile('[a-zA-Z]+')
m = p.match('101011110010')

if m:
    print('Match found: ', m.group())  # match 결과값이 있을 때 실행
else:
    print('No match')  # match된 결과값이 없을 때 실행 (None)

print(m)