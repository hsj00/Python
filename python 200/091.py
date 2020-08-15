# 091 counting char in string
# 092 find specific char/str position in string
# 093 string separate from specific char/str
# 094 string join with specific char
# 095 specific char/str replaces in string


# 091 count
txt = 'A lot of Things occur each day, every day.'

w_count1 = txt.count('o')
w_count2 = txt.count('day')
w_count3 = txt.count(' ')

print(w_count1)
print(w_count2)
print(w_count3)

# 092 find
txt = 'A lot of Things occur each day, every day.'

offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)
offset4 = txt.find('python')

print(offset1)
print(offset2)
print(offset3)
print(offset4)

# 093 split
url = 'https://tv.naver.com/v/12971673'
log = 'name:DREAMCATCHER type:IDOL member:7 genre:K-POP'

ret1 = url.split('/')
print(ret1)

ret2 = log.split()                  # str.split() -> default, space
for data in ret2:
    d1, d2 = data.split(':')
    print('%s -> %s' % (d1, d2))

# 094 join
loglist = ['2020/07/26 20:06', '200', 'OK', '이것 또한 지나가리라']
bond = ';'
# str.join(args) -> arguments is only iteration type available.
# log = bond.join(loglist)
log = ';'.join(loglist)
print(log)

# 095 replace
txt = "Minky's B-day is 970729."

ret1 = txt.replace('0', 'O')
ret2 = txt.replace('-', '')

print(ret1)
print(ret2)

txt = '매일 많은 일들이 일어납니다.'

ret3 = txt.replace('매일', '항상')
ret4 = ret3.replace('일', '사건')

print(ret3)
print(ret4)
