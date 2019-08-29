# Q9, sys.argv

import sys
a = sys.argv
del a[0]

sum = 0
for i in range(0, len(a)):
    sum += int(a[i])

print(sum)