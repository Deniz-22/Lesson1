import math
import sys

print('Введите число от 3 до 20: ')
a = int(input())
if a < 3 or a > 20:
    print('Введено неверное число')
    sys.exit()
for i in range(1, math.ceil(a / 2)):
        for j in range(i + 1, a):
            if ((i + j) % a == 0 or a % (i + j) == 0):
                print(i, j, end=" ")