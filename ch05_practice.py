# Q1 Calculator class

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCal(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCal()
cal.add(10)
cal.minus(7)

print(cal.value)

# Q2 MaxLimitCal

class MaxLimitCal(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCal()
cal.add(50)
cal.add(60)

print(cal.value)