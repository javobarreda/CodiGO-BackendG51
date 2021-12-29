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

#Tuplas , ahora veremos que hay en ellas
alumnos=('Javier','Humberto','Lorena','Maria Paz')

#Ejemplo:

CONFIGURACION=(
    {
        'Nombre':'API_KEY',
        'Valor':'XXX.XXXXX.XXX'
    },
    {
        'Nombre':'Sendgrid',
        'Valor':'Infinito'
    })
#Si una tupla tiene internamente una estructura de datos cambiable, si se podra cambiar.
#En cambio si hay dato primitivo como STR, INF, etc Ahi si no se puede.

CONFIGURACION[0]['Nombre']='XD'
CONFIGURACION=('76876234234','781273912312','9875677623')


print(CONFIGURACION)
print(CONFIGURACION[1])
#DICCIONARIOS:
#Coleccion de elementos que estan inexados y cuentan con una llave o clave y su valor de contenido
# se puedne modificar el contenido y ademas s epuede crear nuevas llaves

persona= {
    'nombre':'Javier',
    'correo':'javier.barreda@utec.edu.pe',
    'inversiones':[
        {
            'fuente':'binance',
            'tipo':'bitcoin'
        },
        {
            'fuente':'netmask',
            'tipo':'NFT'
        }
    ],
}
#podemos agregar una nueva seccion al diccionario:
persona['estatura']='1.72'
print(persona.keys())
print(persona.values())