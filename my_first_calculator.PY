def add(number1 , number2):
    return number1 + number2

def sub(number1 , number2):
    return number1 - number2

def mul(number1 , number2):
    return number1 * number2

def div(number1 , number2):
    try:
        return number1 / number2
   
    except ZeroDivisionError:
        return print('You cant divide by 0')

inp = input('Select your operation: /,*,+,- \nyour selection -> ')
number1 = int(input('Enter number one: '))
number2 = int(input('Enter number two: '))

total = 0 
if inp == '/':
    total = div(number1, number2)
    print(f'The result is: {total}')

elif inp == '*':
    total = mul(number1, number2)
    print(f'The result is: {total}')

elif inp == '+': 
    total = add(number1 , number2)
    print(f'The result is: {total}')

elif inp == '-':
    total = sub(number1 , number2)
    print(f'The result is: {total}')

