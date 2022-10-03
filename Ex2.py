#  Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
# import math
# a = int(input('Введите коэф  a '))
# b = int(input('Введите коэф  b '))
# c = int(input('Введите коэф  c '))
# d=b**2-4*a*c
# print(d)
# x1 = (-b + math.sqrt(math.fabs(d)))/2*a
# x2 = (-b - math.sqrt(math.fabs(d)))/2*a
# print (f'x1 = {x1} и x2 = {x2}')

# from sympy.solvers import solve
# from sympy import symbol

import sympy
x = sympy.Symbol('x')
a = int(input('Введите коэф  a '))
b = int(input('Введите коэф  b '))
c = int(input('Введите коэф  c '))
d = a*x**2+b*x+c
ans = sympy.solve(d, x)
print(ans)
