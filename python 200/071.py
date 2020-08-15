# 정수 리스트에서 소수만 걸러내기
"""
def getPrime(x):
      if x % 2 == 0:
    return

  for i in range(3, int(x/2), 2):
    if x % i == 0:
      break

  else:
    return x

listdata = [117, 119, 1113, 11113, 11119]
ret = filter(getPrime, listdata)
print(list(ret))
"""

# 정수 n 이하의 모든 소수를 구하는 함수


def getPrime(n):
    ret = [2]
    if n == 1:
        return print("integer '1' is not a prime number.")

    elif n == 2:
        return ret

    for i in range(3, n + 1, 2):
        for k in range(3, int(i/2), 2):
            a = i % k
            if a == 0:
                break

        else:
            ret.append(i)
    return ret


ret = getPrime(10)
print(ret)

ret = getPrime(1)
print(ret)
