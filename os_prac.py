# Q10, os function

import os

os.chdir("d:/")
os.system("dir")
a = os.popen("dir")
print(a.read())