# 075 char extract from specific position in string
# 076 string extract from specific range in string
# 077 oddth char extract from string
# 078 string reversing
# 079 string sum
# 080 string repeating

txt1 = 'A tale that was not right'
txt2 = '이것 또한 지나가리라'

# 075
print(txt1[5])              # 4번째 문자, 5 미만에서의 위치
print(txt2[-2])             # 뒤에서 두 번째 문자

# 076
print(txt1[3:7])            # 3 이상, 7 미만
print(txt1[:6])             # 처음부터 6 미만까지
print(txt2[-4:])            # 뒤에서 네 번째 문자부터 끝까지

# text print loop
txt = 'python'
for i in range(len(txt)):   # 문자열 길이만큼 for문 반복
    # 문자열 길이 +1을 해서 범위를 지정하여 문자열 출력 -> [a:b:c], a 이상 b 미만까지 c의 간격으로
    print(txt[:i+1])

# 077 oddth char extracting
txt = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
o_ret = txt[::2]        # 0번째 문자부터 1칸 건너띄기
e_ret = txt[1::2]       # 1번째 문자부터 1칸 건너띄기
print(o_ret)
print(e_ret)

# 078 reversing
ret01 = txt[::-1]       # 처음부터 끝까지, 뒤에서부터
ret02 = txt[::-2]       # 처음부터 끝까지, 뒤에서부터 1칸 건너띄며
ret03 = txt[-2::-2]     # 뒤에서 두번째부터, 뒤에서부터 1칸 건너띄며
print(ret01)
print(ret02)
print(ret03)

# 079
filename = input('What is the file name?: ')
filename = filename + '.jpg'
display_msg = "That file name is <" + filename + ">."
print(display_msg)

# 080
msg01 = "Hey everyone!"
msg02 = "Hurry up!"
display_msg = msg01 + " " + (msg02 + " ")*3 + "!!"
print(display_msg)
