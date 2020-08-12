# https://wikidocs.net/3096
# practice problems 04

# 4-1
for i in range(5):
    print("*", end="")

# 4-2
"""
for i in range(0, 4):
    print("\n")
    for j in range(0, 5):
        print("*", end="")
"""
for i in range(4):
    for j in range(5):
        print("*", end="")
    print("")

# 4-3
"""
for i in range(1, 6):
    print("*" * i, end="\n")
"""

for i in range(5):
    print("*" * (i + 1), end="\n")

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print("")

# 4-4
for i in range(1, 6):
    print("*" * (6 - i), end="\n")

for i in range(5):
    print("*" * (5 - i), end="\n")

for i in range(5):
    for j in range(5 - i):
        print("*", end="")
    print("")

# 4-5
for i in range(5):
    print(" " * (5 - i) + "*" * i, end="\n")

for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print("")

# 4-6
for i in range(5):
    print(" " * i + "*" * (5 - i), end="\n")

for i in range(5):
    for j in range(i):
        print(" ", end="")
    for j in range(5 - i):
        print("*", end="")
    print("")

# 4-7
for i in range(5):
    print(" " * (5 - i) + "*" * (2 * i + 1))

for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print("")

# 4-8
for i in range(5):
    print(" " * i + "*" * (2 * (5 - i) - 1) + " " * i)

for i in range(5):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (5 - i) - 1):
        print("*", end="")
    print("")

# 4-9
apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for floor in apart:
    for i in floor:
        if i in arrears:
            pass

        else:
            print(i, "is received newspaper!")


for floor in apart:
    for i in floor:
        if i in arrears:
            continue

        else:
            print(i, "is received newspaper!")
