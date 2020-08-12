# wikidocs practice
# https://wikidocs.net/3144

# 5-1
def myaverage(a, b):
    return (a + b) / 2


# 5-2
def get_max_min(data_list):
    max_data = max(data_list)
    min_data = min(data_list)
    return (max_data, min_data)


# 5-3
import os


def get_txt_list(path):
    txt_list = []
    txt_path = os.listdir(path)
    for file in txt_path:
        if file.endswith(".txt"):
            txt_list.append(file)
    return txt_list


# 5-4
def BMICal(weight, height):
    BMI = weight / ((height * 0.01) ** 2)
    if BMI < 18.5:
        return print("Thin")
    elif 18.5 <= BMI < 25.0:
        return print("Standard")
    elif 25 <= BMI < 30.0:
        return print("Obese")
    else:
        return print("Seriously Obese")


# 5-5
def BMICal02():
    height = input("Your height: ")
    weight = input("your weight: ")
    BMI = float(weight) / ((float(height) * 0.01) ** 2)
    if BMI < 18.5:
        return print("Thin")
    elif 18.5 <= BMI < 25.0:
        return print("Standard")
    elif 25 <= BMI < 30.0:
        return print("Obese")
    else:
        return print("Seriously Obese")


# 5-5 solution
def cal_bmi2(height, weight):
    height = height * 0.01
    bmi = weight / (height * height)
    print("BMI: ", bmi)
    if bmi < 18.5:
        print("마른체형")
    elif 18.5 <= bmi < 25.0:
        print("표준")
    elif 25.0 <= bmi < 30.0:
        print("비만")
    else:
        print("고도비만")


while 1:
    height = input("Height (cm): ")
    weight = input("Weight (kg): ")
    cal_bmi2(float(height), float(weight))


# 5-6
def get_triangle_area(width, height):
    return (width * height) / 2


# 5-7
def add_start_to_end(start, end):
    return sum(range(start, end + 1))


# 5-8
cities = ["Seoul", "Daejeon", "Daegu", "Kwangju", "Busan", "Jeju"]


def threeLetter(data):
    tL = []
    for i in data:
        tL.append(i[:3])
    return tL
