# 045 module import
# 046 from/import
# 047 import/as

# 045
"""
import time
import mylib
import mypackage.mylib

time.sleep(1)
mylib.add_txt('KOR', 'GER')
mypackage.mylib.reverse(1, 2, 3)
"""

# 046
"""
from time import sleep
from mypackage import mylib             # from 패키지 이름 import 모듈 이름
from mypackage.mylib import reverse     # from 모듈 이름 import 함수 이름

sleep(1)
mylib.add_txt('KOR', 'GER')
reverse(1, 2, 3)
"""

# 047
"""
import mypackage as mp          # import 이름이 긴 모듈명 as 축약명
import mypackage.mylib as ml

ret1 = mp.mylib.add_txt('KOR', 'GER')
ret2 = ml.reverse(1, 2, 3)

print(ret1)
print(ret2)
"""
