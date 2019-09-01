# Q11 time module
## YYYY/MM/DD hh:mm:ss

import time

## Sun Sep  1 19:05:52 2019
a = time.strftime('%c', time.localtime(time.time()))
print(a)


## Sun Sep  1 19:05:52 2019
b = time.asctime(time.localtime(time.time()))
print(b)

## 09/01/19 19:05:52
c = time.strftime('%x %X', time.localtime(time.time()))
print(c)