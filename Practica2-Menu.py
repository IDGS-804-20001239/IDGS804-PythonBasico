import os

class Operasbas():
    #Propiedades de clase
    num1=0
    num2=0
    res=0
    #constructor de la clase
    def __init__(self, a,b):
        self.num1=a
        self.num2=b
    #Se utiliza (self) solo si va dentro de la clase
    def suma(self):
        self.res=self.num1+self.num2 
        print("La suma es: {}".format(self.res))

    def resta(self):
        self.res=self.num1-self.num2
        print("La resta es: {}".format(self.res))

    def multi(self):
        self.res=self.num1*self.num2
        print("La multiplicacion es: {}".format(self.res))

    def div(self):
        self.res=self.num1/self.num2
        print("La division es: {}".format(self.res))

def main():
        os.system('cls')
        opc = input('1 = Suma, 2 = Resta, 3 = multiplicacion, 4= division, 5 = salir')
        while int(opc != '5'):
            if int(opc == '1'):
                obj = Operasbas(int(input("num1: ")), int(input(("num2: "))))
                obj.suma()
                print(obj.res)
            elif int(opc == '2'):
                obj = Operasbas(int(input("num1: ")),int(input(("num2: "))))
                obj.resta()
                print(obj.res)
            elif int(opc == '3'):
                obj = Operasbas(int(input("num1: ")),int(input(("num2: "))))
                obj.multi()
                print(obj.res)
            elif int(opc == '4'):
                obj = Operasbas(int(input("num1: ")),int(input(("num2: "))))
                obj.div()
                print(obj.res)
            elif int(opc == '5'):
                print('Haz salido')
            else:
                print('NUmero incorrecto')

            opc=input('1 = Suma, 2 = Resta, 3 = multiplicacion, 4= division, 5 = salir')   
 #Indica hasta donde debe de ejecutarse
if __name__ == '__main__':
    main() 