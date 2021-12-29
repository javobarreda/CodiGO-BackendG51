#Los operadores aritmeticos son: suma, resta, multiplicacion, division, exponente, cociente, modulo
numero1=30
numero2=10

resultado=numero1 + numero2
print(resultado)

#el resultado es:

print('El resultado estimadisimo es',resultado)

#La otra forma es usando llave, si ponemos llave es que hay algo despues
#debemos declarar el contenido de esa llave al final.

print('El resultado estimadisimo es {} y ya esta'.format(resultado))
print('El resultado estimadisimo es {} y no {}'.format(resultado, numero1))

print('El resultado estimadisimo no es {1} y es {0}'.format(resultado, numero1))

division1 = numero2 / numero1
print('{:.3f}'.format(division1))


texto = "Buenas, yo soy Javier"
#las variables STR tambien pueden ser accedidas a analizarse como listas

#el modulo
resultado = numero1 % numero2
print('el modulo es',resultado)

#el cociente
resultado = numero1 // numero2
print('el cociente es',resultado)

#el exponente
resultado = numero1 ** numero2
print('el exponente es',resultado)