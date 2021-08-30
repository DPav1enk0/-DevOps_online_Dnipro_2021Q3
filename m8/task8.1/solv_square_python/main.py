# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def main():
    pass


def validate_param_(i):
    try:
        i = int(input("Введите число для проверки: "))
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")
    else:
        if 50 <= int(i) >= -50:
            print("Ваше число не в диапазоне. Попробуйте снова")
        else:
            print("Число в правильном диапазоне.")
            print("Число", i, " является целым")
        return i


def discriminant(a, b, c):
    if a == 0:
        raise ValueError('коэфициент a не может быть 0')
    return (b ** 2) - (4 * a * c)


def roots(d, a, b, c):
    if d < 0:  #D < 0, то корней нет
        print("Дискриминант < 0")
        print("Корней нет")
    elif d == 0:  #Если d = 0, то корень 1
        x = (-b + math.sqrt(d)) / (2 * a)
        print("Корень один: ", x)
        return x
    else:  #Если    D > 0, то    2    корня
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Есть 2 корня: ")
        print("Корень 1 =  ", round(x1, 3))
        print("Корень 2 =  ", round(x2, 3))


def solv_square():
    pass


def square_print(a, b, c, roots):
    print('Дискриминант = ', d)


# main program
n1 = float(input("введите первое число "))
n2 = float(input("введите второе число "))
n3 = float(input("введите третье число "))
d = discriminant(n1, n2, n3)
validate_param_(i=int)
square_print(n1, n2, n3, roots(d, n1, n2, n3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
