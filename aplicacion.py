from flask import Flask, render_template,request

app = Flask(__name__, template_folder='templates')




@app.route('/')
def home_pagina():
    return 'Pagina inicial'



@app.route('/info')
def info():
    return 'Este es un servidor de Flask'


@app.route('/saluda/<nombre>')
def saludar(nombre):
    return 'hola, como estas {} ?'.format(nombre)

@app.route('/pagina')
def pagina():
    
    personas = [{
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': 25}, 
            {
    'nombre': 'Pedro',
    'apellido': 'Carrasco',
    'edad': 55}, 
            {
    'nombre': 'Mario',
    'apellido': 'Villarroel',
    'edad': 44}]

    arreglo_simple = ['mouse', 'teclado', 'monitor', 'impresora', 'raton']
    
    return render_template('index.html', 
                           variable_uno="Pedro", 
                           personas=personas, 
                           arreglo_simple=arreglo_simple)
    

@app.route('/sumar/<int:a>/<int:b>', methods=['GET'])
def sumar(a, b):
    response = {
        'operacion': 'suma',
        'sumanado1': a,
        'sumanado2': b,
        'resultado': a + b,
    }
    
    return response

@app.route('/dividir/<int:a>/<int:b>', methods=['GET'])
def dividir(a, b):
    response = {}
    try:
        
        response = {
            'operacion': 'dividir',
            'sumanado1': a,
            'sumanado2': b,
            'resultado': a / b,
        }


    
    except Exception as e:
        response = {
            'Mensaje': 'Error: {}'.format(e),
            'operacion': 'dividir',
        }
    
    
    return response



@app.route('/sumar/post', methods=['POST'])
def sumar_post():
    parametros = request.get_json()
    a = parametros['a']
    b = parametros['b']
    response = {
        'operacion': 'suma',
        'sumanado1': a,
        'sumanado2': b,
        'resultado': a + b,
    }
    
    return response