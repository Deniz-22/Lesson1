number1 = int(input('Введите число1: '))
number2 = int(input('Введите число2: '))
number3 = int(input('Введите число3: '))
if number1 == number2 and number1 == number3:
    print(3)
elif number1 == number2 or number2 == number3:
    print(2)
else:
    print(0)