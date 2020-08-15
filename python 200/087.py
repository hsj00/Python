# 087 upper/lower
# 088 remove the side space in string
# 089 string to int/float
# 090 numbet to string

# 087
txt = "A lot of things occur each day."

ret1 = txt.upper()
ret2 = txt.lower()

print(ret1)
print(ret2)

# 088 lstrip/rstrip/strip
txt = '  It has vacancy letters on sides.  '

ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()

print('<' + txt + '>')
print('<' + ret1 + '>')
print('<' + ret2 + '>')
print('<' + ret3 + '>')

# 089 int/float
numstr = input('Enter the number: ')
try:
    num = int(numstr)
    print('The number that you type is integer <%d>.' % num)
except:
    try:
        num = float(numstr)
        print('The number that you type is float number <%f>.' % num)
    except:
        print('+++ Please enter only number. +++')

# 090 str
num1 = 1234
num2 = 3.141592

numstr1 = str(num1)
numstr2 = str(num2)

print("'num1' to str transfer value is '%s'." % numstr1)
print("'num2' to str transfer value is '%s'." % numstr2)
