# import math
#
# def foo(x):
#     return x - 2 + math.e**x
#
# def foo1(x):
#     return math.e**x + 1
#
# # def foo(x):
# #     return 2**x - 2*x**2 + 1
# #
# # def foo1(x):
# #     return 2 - 4*x
#
# a = -10
# b = 10
# q = 100
# eps = 0.0001
# count = 0
# count1 = 0
# # while abs(a - b) > eps:
# while count < 3: # Дихотомии
#     sred = (a + b) / 2
#     a1 = foo(a)
#     b1 = foo(b)
#     sred1 = foo(sred)
#     if sred1 < 0 and a1 < 0:
#         a = sred
#     if sred1 > 0 and b1 > 0:
#         b = sred
#     count += 1
#
# while abs(q - b) > eps: # Ньютона
#     q = b
#     b = b - (foo(b) / foo1(b))
#     count1 += 1
#
#
# print('Ответ:', b)
# print('F(x) =', foo(b))
# print('Кол-во итераций Дихотомии:', count)
# print('Кол-во итераций Ньютона:', count1)



# # Отдельно Ньютон
# import math
#
# def foo(x):
#     return x - 2 + math.e**x
#
# def foo1(x):
#     return math.e**x + 1
#
# # def foo(x):
# #     return 2**x - 2*x**2 + 1
# #
# # def foo1(x):
# #     return 2 - 4*x
#
# a = -10
# b = 10
# q = 100
# eps = 0.0001
# count = 0
# count1 = 0
#
#
# while abs(q - b) > eps: # Ньютона
#     q = b
#     b = b - (foo(b) / foo1(b))
#     count1 += 1
#
#
# print('Ответ:', b)
# print('F(x) =', foo(b))
# print('Кол-во итераций Ньютона:', count1)




# # Отельно Дихотомия
# import math
#
# def foo(x):
#     return x - 2 + math.e**x
#
# def foo1(x):
#     return math.e**x + 1
#
# # def foo(x):
# #     return 2**x - 2*x**2 + 1
# #
# # def foo1(x):
# #     return 2 - 4*x
#
# a = -10
# b = 10
# q = 100
# eps = 0.0001
# count = 0
# count1 = 0
# while abs(a - b) > eps:
#     sred = (a + b) / 2
#     a1 = foo(a)
#     b1 = foo(b)
#     sred1 = foo(sred)
#     if sred1 < 0 and a1 < 0:
#         a = sred
#     if sred1 > 0 and b1 > 0:
#         b = sred
#     count += 1
#
#
#
# print('Ответ:', (a + b) / 2)
# print('F(x) =', foo((a + b) / 2))
# print('Кол-во итераций Дихотомии:', count)







#2 задание
import math
eps = 0.0001
count = 0
def foo1(x, y):
    return -x + math.sin(y + 0.5) - 1


def foo2(x, y):
    return math.cos(x - 2) + y
#
#
# def foo11(x):
#     return math.cos(y + 0.5) - 1
#
#
# def foo22(x):
#     return 1 - math.sin(x - 2)

def foo01(y):
    return math.cos(y + 0.5)

def foo00(x):
    return -1

def foo10(x):
    return -math.sin(x - 2)

def foo11(y):
    return 1

x = -0.5 # Приближение
y = 0.5 # Приближение

M = []
while True:
    M = [[foo00(x), foo01(y)], [foo10(x), foo11(y)]]


    F1 = -foo1(x, y)
    F2 = -foo2(x, y)

    detw = (M[0][0] * M[1][1]) - (M[0][1] * M[1][0])
    detw1 = (F1 * M[1][1]) - (F2 * M[0][1])
    detw2 = (F2 * M[0][0]) - (F1 * M[1][0])

    delta_x = detw1 / detw
    delta_y = detw2 / detw

    x = x + delta_x
    y = y + delta_y

    count += 1

    if abs(delta_x) < eps and abs(delta_y) < eps:
        break

print('x:', x, 'y:', y)
print('Итераций:', count)
