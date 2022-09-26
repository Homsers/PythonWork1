a = float(input('Enter a first number '))
b = float(input('Enter a second number '))
o = input('Enter an operation ')

result = 0


if o == "+":
    result = a + b
elif o == "-":
    result = a - b
elif o == "*":
    result = a * b 
elif o == "**":
    result = a ** b 
elif o == "%" and b == 0:
    print('делить на 0 нельзя!!!')
elif o == "%" and b != 0 :
    result = a % b 
elif o == "//" and b == 0:
    print('делить на 0 нельзя') 
elif o == "//" and b != 0:
    result = a // b 
elif o == "/" and b == 0:
    print('делить на 0 нельзя!')
elif o == "/" and b != 0:
    result = a / b


print(f"{result}")

    

