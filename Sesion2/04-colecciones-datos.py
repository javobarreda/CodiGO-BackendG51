#Días

dias = ['Lunes','Martes', 'Miercoles']
dias.append('Jueves')
print(dias)

dias.remove('Lunes')
print(dias)
dias.clear()
print(dias)

#variables mutables y no mutables:

lista1 = [1,2,3,4,5]
lista2 = lista1
lista3 = lista1[:]
lista1[0]=38
print(id(lista1))
print(id(lista2))
print(id(lista3))
print('La lista 1 es', lista1)
print('La lista 2 es', lista2)
print('La lista 3 es', lista3)