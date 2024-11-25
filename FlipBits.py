def totalflips(num1, num2):
    flips = 0
    while(num1 > 0 or num2 > 0):
        t1 = num1 & 1
        t2 = num2 & 1
        if t1 != t2:
            flips += 1

        num1 >>= 1
        num2 >>= 1

    return flips

num1 =int(input('enter the first number: '))
num2 =int(input('enter the second number: '))

print('\n')

print('(first number) = ',num1)
print('(second number) = ',num2)

print('\n')

print('number of flips needed: ', totalflips(num1,num2))