# wikidocs practice
# https://wikidocs.net/3452

# 7-1
f = open("/Users/anartanimal/Documents/Python/wikidocs/practice.txt", "wt")
for i in range(1, 11):
    f.write("%d\n" % i)
f.close()

# 7-2
def mkList(path):
    import os

    f = open(str(path) + "mkList.txt", "wt")
    lists = os.listdir(path)
    for list in lists:
        f.write("%s\n" % list)
    f.close()


mkList("/Users/anartanimal/Documents/Python/")
