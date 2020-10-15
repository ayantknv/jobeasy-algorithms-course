num1 = int(input(f'first number '))
num2 = int(input(f'second number '))
num3 = int(input(f'third number '))

def max_of_three(number_1, number_2, number_3):
    if number_1 > number_3 and number_1 > number_2:
            return number_1
    elif number_2 > number_1 and number_2 > number_3:
            return number_2
    else:
            return number_3


print(max_of_three(num1, num2, num3))