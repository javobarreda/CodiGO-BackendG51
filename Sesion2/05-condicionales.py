#CONDICIONALES IF ELSE
edad=30
edad_minima=18

if edad >=edad_minima:
     print('Eres mayor de edad, adelante chavo')
elif edad>15:
    print('Puedes ingresar a las justas pero nada con alcohol')
elif edad>13:
    print('Eres un niño, pero puede haber una excepcion')
else:
    print('Eres muy menor, no puedes ingresar')

print('eres mayor de edad') if edad >= edad_minima else print ('no eres tan mayor, eres menor de edad')

#Tambien puedes guardarlo en una variable:
resultado ='eres mayor de edad' if edad >= edad_minima else'no eres tan mayor, eres menor de edad'
print(resultado)

#tengo el siguiente numero
numero = 13

# cómo saber si es para o impar?

respuesta = 'es par' if numero %2 == 0 else 'es impar'
print(respuesta)

persona={
    'nombre':'Javier',
    'nacionalidad':'argentina',
    'sexo':'M'
}
print('El nombre de la persona es',(persona['nombre']), 'y su nacionalidad es',(persona['nacionalidad']))

if (persona['nombre'] == 'Javier' and persona['nacionalidad']=='peruana'):
    print('Si, el nombre de la persona es',(persona['nombre']), 'y su nacionalidad es', persona['nacionalidad'])
else:
    print('No, el nombre de la persona es',(persona['nombre']), 'y su nacionalidad es', persona['nacionalidad'])

#Vamos con el FOR:
#Ejemplo:

meses =['Enero','Febrero','Marzo','Abril']
for mes in meses:
    if mes == 'Enero':
        print('Vamos a la playa')
    print(mes)
#va de 2 en 2 y de 5 a 10.
for numero in range(5,10,2):
    print(numero)


# aqui tenemos iteracion de numeros en un rango y con la extensión reptitiva (o se acuantos salen respecto a la extension de elementos en la lsita meses)
for numero in range(len(meses)):
    print(numero)


# ahora si lo queremos a la mitad de la lista:
for numero in range(int(len(meses)/2),len(meses)):
    print(numero)
#NO SALDRA ERROR porque sale decimal. ENTONCES CONVERTIMOS EN ENTERO.