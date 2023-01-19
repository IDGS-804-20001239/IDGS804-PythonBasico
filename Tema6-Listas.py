lista1=["Yair",1,2,23,True]

print(lista1)

print(lista1[:])
print(lista1[2:4])
print(lista1[:2])
print(lista1[3:])

#Valor al final
lista1.append("Yair")
print(lista1)
#Reemplaza el valor
lista1.insert(0,"Mario")
print(lista1)
#Añadir
lista1.extend([0,10,11])
print(lista1)
print(lista1.index("Yair"))
#Remover
lista1.remove("Yair")
print(lista1)

lista1.pop()
print(lista1)