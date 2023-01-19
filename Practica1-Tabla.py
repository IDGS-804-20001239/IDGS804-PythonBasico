num1= int(input('Ingresa un numero'))

def tabla(num2):
    for x in range(1,11):
        print("{0} x {1} = {2}".format(num2, x, num2 * x))
    
tabla(num1)