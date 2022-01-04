from flask import Flask, request
# el request nos da toda la información del cliente: hora de solicitud, info, método al cual quiere acceder el cliente.

app = Flask(__name__)

mis_productos = [{
    "nombre": "Paneton con arto bromato",
    "precio": 17.50,
    "disponible":True,
    "fecha_vencimiento":"2022-01-12"

},{
    "nombre": "Paneton con chocolate con arta azucar",
    "precio": 15.50,
    "disponible":False,
    "fecha_vencimiento":"2022-12-30"
}]
    

#endpoint. NO SE DICE URL. el URL es el dominio + endpoint
@app.route('/', methods=['POST','GET'])
def inicio():
    # REQUEST.method nos da el metodo que esta queriendo acceder el cliente Y cómo podriamos ver si e sun post o un get.
    #Y como sabemos si es GETO o POST?
    print(request.method)

    if request.method =='POST':
    # Captura lel json enviado por el cliente y lo convierte a un diccionario para que python lo entienda.
        print (request.get_json())
    # validar si hay el nombre y si lo hay entonces retornar un saludo con ese nombre: Hola, Javier!
    # SI no hay nombre, entonces indicar que falta info: ESTADO 400
        data = request.get_json()
        #guardo diccionario en variable llamada data
        if(data.get('nombre')):
            #si hay variable nombre en data entonces
            nombre = data.get['nombre']
            return 'Hola,{}!'.format(nombre)
        else:
            return 'Necesito la info',400

    elif request.method =='GET':
        return  'Bienvenido a mi API de productos', 200

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method =='GET':
        return {
            'data': mis_productos,
            'message': 'Los productos son',
            'ok': True
        }

    elif request.method =='POST':
        data = request.get_json()
        mis_productos.append(data) #aqui estamos insertando un registro en una base de datos. Abajo no imrpota el orden porque etamos dentro de un diccionario. Asi que chill
        return {
            'data':data,
            'message': 'Producto agregado exitosamente',
            'ok':True
        }, 201
# al ponerle el tipo de dato y al enviar no es el tipo de datos, se rechazará automaticamente la peticion con un 404 NOT FOUND. le hemos metido int para definir el tipo de variable.
@app.route('/producto/<int:id>', methods=['GET'])
def producto(id):
    if request.method=='GET':
        #Solucion del problema
        if(id < len(mis_productos)):
            return {
                'ok':True,
                'data':mis_productos[id],
                'message':'El producto es:'
            }
        else:
            return {
                'ok':False,
                'data':None,
                'message':'El producto no existe:'
            }

if __name__=='__main__':
    app.run(debug=True)

# Si es que name igual a main recien ingresamos a la línea 6. Pero si es un archivo seundario, NO podra levantar el proyecto, entonces no se usará FLASK. Es para validar el proyecto. 

