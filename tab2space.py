# tab2space.py
# 1 tab = 4 spaces converter

## python tab2space.py src dst
## python tab2space.py a.txt b.txt


import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_cont = f.read()
f.close()

space_cont = tab_cont.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_cont)
f.close()