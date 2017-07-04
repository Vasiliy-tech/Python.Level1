author = 'Аминов Карим Салимжонович'
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
x = int(input("Введите целое число = "))
su = len(str(x))
z = 0
n = 0
while n < x:
   y = x % 10
   x = x // 10
   if z < y:
       z = y
   else:
       z = z
print("Наибольшая цифра в числе = ", z)
print("Количество цифр в числе = ", su)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
a = input("Введите значение первой переменной А = ")
b = input("Введите значение второй переменной В = ")
a,b = b,a
print("Поменяем значения переменных местами.\nТеперь значение переменной А = ", a, ", а значение переменной В = ", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
a = float(input("Для решения квадратного уравнения (вида ax2 + bx + c = 0) введите число A = "))
b = float(input("Введите число B = "))
c = float(input("Введите число C = "))
d = b * b - 4 * a * c
if d > 0:
    x1 = float((-b + math.sqrt(d)) / (2 * a))
    x2 = float((-b - math.sqrt(d)) / (2 * a))
    print("Квадратные корни из уравнения X1 = ", x1, " X2 = ", x2)
elif d == 0:
    x = -b / (2 * a)
    print("Квадратный корень равен X = ", x)
else:
    print("Квадратные корни в уравнении отсутствуют")