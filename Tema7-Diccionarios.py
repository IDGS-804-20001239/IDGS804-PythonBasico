miDiccionario = {"Matricula": 123456,"Apellidos":"Terán"}

print(miDiccionario["Apellidos"])
miDiccionario["Materia"]="DWP"
print(miDiccionario)
miDiccionario["Matricula"]=98765
print(miDiccionario)
del miDiccionario["Apellidos"]
print(miDiccionario)