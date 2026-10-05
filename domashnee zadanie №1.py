# ####### 1. Выведите на экран следующую последовательность чисел с помощью цикла while.
# #
# # 3
# #
# # 13
# #
# # 23
# #
# # 33
# #
# # 43
#
# num = 3
# while num <= 43:
#     print(num)
#     num += 10
#
#
#
# ####### 2. Напишите программу для проверки длины введенного пароля с использованием цикла while.
# # Программа должна запрашивать у пользователя ввод пароля и проверять его длину.
# # Длина пароля должна быть не менее 8 символов.
#
# num = input("Введите пароль\n")
# while len(num) < 8:
#     print("Длина пароля должна составлять 8 символов")
#     num = input("Введите пароль\n")
# print("Пароль принят.")
#
#
#
# ####### 3. Пользователь должен ввести вот такую строку с параметрами автомобиля:
# # “LADA 2010г 205000км 450000руб”. Программа с помощью одной f-строки с символами
# # переноса строки “\n” должна вывести несколько строк с информацией о продаже автомобиля.
#
# print(f"Введите параметры автомобиля по шаблону\n"
#       f'LADA 2010г 205000км 450000руб')
# model = input('Введите модель авто\n').upper()
# year = int(input('Введите дату выпуска авто\n'))
# mileage = int(input('Введите пробег авто\n'))
# cost = int(input('Введите стоимость авто\n'))
#
# print(f"Продается автомобиль\n"
#       f"Марка: {model}\n"
#       f"Год выпуска: {year}г\n"
#       f"Пробег: {mileage}км\n"
#       f"Цена: {cost}руб")
#
#

# a, b, c = map(int, input().split())
#
# print((b+a)-c)

# s, d = map(int, input().split())
# print(s + d)
#
# days, pay = map(int, input().split())
# print(days // pay, days % pay)


# a, b, c = map(int, input().split())
#
# print(a-c, b, (a+b+c))


# a, b = map(int, input().split())
# if a<0:
# 	a = a * (-1)
# if b<0:
# 	b = b * (-1)
# print(a+b)


# a, b, k = map(int, input().split())
# if abs(a - b) <= k:
#     print("OK")
# else:
#     print("FLAG")

# num = int(input())
# list = list(map(int, input().split()))
# print(sum(list))

# num = list(map(int, input().split()))
# print(num)
