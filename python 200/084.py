# 084 string check (isalpha)
# 085 string check (isdigit)
# 086 string check (isalnum)

# 084 alphabet check in str
txt1 = 'A'                      # english letter
txt2 = '안녕'                    # korean text
txt3 = 'World of Warcraft'      # space between words
txt4 = 'C3PO'                   # includes number

ret1 = txt1.isalpha()
ret2 = txt2.isalpha()
ret3 = txt3.isalpha()
ret4 = txt4.isalpha()

print(ret1)
print(ret2)
print(ret3)
print(ret4)

# 085 digit check in str
txt1 = '010-1234-5678'          # includes '-'
txt2 = 'R2D2'                   # includes alphabet letters
txt3 = '0729'                   # it only consists of integer number
# txt4 = 970729               # integer, 'int' object has no attribute 'isdigit'

ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()
## ret4 = txt4.isdigit()

print(ret1)
print(ret2)
print(ret3)
# print(ret4)

# 086 alphbet or number check in str
txt1 = 'Hi there?'                  # space, question mark
txt2 = '1. Title-input the title'   # period mark, space
txt3 = 'C3피오R2D2'                  # alphabet letters and number

ret1 = txt1.isalnum()
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()

print(ret1)
print(ret2)
print(ret3)
