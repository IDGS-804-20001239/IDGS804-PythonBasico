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
    
    def resta(self):
        self.res=self.num1-self.num2

    def multi(self):
        self.res=self.num1*self.num2
    def div(self):
        self.res=self.num1/self.num2
def main():
        os.system('cls')
        obj=Operasbas(3,4) 
        obj.suma()
        print('La suma es: {}'.format(obj.res))

    #Indica hasta donde debe de ejecutarse
if __name__ == '__main__':
    main() 

    #Metodos de clase
