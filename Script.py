input1 = int(input("Please Enter your first Number"))
input2 = int(input("Please Enter your first Number"))
input3 = int(input("What operation shall be used?"))


def add(a, b):
    summa = a + b
    print(summa)


def sub(a, b):
    dif = a-b
    print(dif)


def mul(a, b):
    product = a*b
    print(product)


def div(a, b):
    quotient = a / b
    print(quotient)


if input3 == '+':
    add(input1, input2)

else:
    if input3 == '-':
        sub(input1, input2)

    if input3 == '*':
        mul(input1, input2)

    if input3 == '/':
        div(input1, input2)
