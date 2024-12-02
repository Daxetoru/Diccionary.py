palabras_diccionario = {'Caneca':'Objeto donde se tiran los desechos', 'Pilo':'Persona inteligente o astuta',
                       'Peluquear':'Acción de recortarse el pelo','Chino':'Digase de un niño pequeño',}

for i in range(5):
    definicion = input('Que palabra no entiendes?:')
    if definicion in palabras_diccionario.keys():
        print(definicion,'significa:', palabras_diccionario[definicion])
    else:
        print('Yo tampoco conozco esa palabra!')
