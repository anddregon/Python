#* ->
#* -> Estructura de datos mutables que funcionan con llave:valor (key:value)
#* -> Los elementos se separan por comas.
#* -> Funcionan como un diccionario de la vida real
#* -> Al igual que en los Set, en los diccionarios no existen indices
#*    para eso usamos las llaves (keys).


def main():
    diccionario = {
        'IDE':'Integrated Development Enviroment',
        'OOP':'Object Oriented Programming',
        'DBMS':'Database Management System'
    }

    print (f'Mi diccionario: {diccionario}')

    #Largo
    print(f'\nNúmero de elementos del diccionario: {len(diccionario)}')

    #acceder a un elemento (key)
    print('\nValor de la llave IDE:')
    print(diccionario['IDE'])

    #Otra forma de recuperar un elemento
    print('\nValor de la llave OOP:')
    print (diccionario.get('OOP'))

    #Modificar elementos
    diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
    print(f'\nCambio del valor de la llave IDE: {diccionario}')

    #Recorrer elementos
    print('\nRecorrer Diccionario: ')
    for llave, valor in diccionario.items():
        print(f'{llave}: {valor}')

    #Recolver solo llaves
    print('\nDevolver solo llaves: ')
    for llave in diccionario.keys():
        print(llave)

    #Recolver solo llaves
    print('\nDevolver solo valores: ')
    for valor in diccionario.values():
        print(valor)

    # Comprobar existencia de elemento mediante llave
    print('\n¿Existe elemento de llave IDE?')
    print('IDE' in diccionario)

    #Agregar elemento
    #No es posible agregar llaves duplicadas, si agregamos una llave existente
    #sobreescribe la llave con el nuevo valor
    diccionario['PK'] = 'Primary Key'
    print(f'\nNuevo elemento añadido: {diccionario}')

    #Remover un elemento
    diccionario.pop('DBMS')
    print(f'\nDiccionario con elemento removido:  {diccionario}')

    #Limpiar diccionario
    diccionario.clear()
    print(f'\nDiccionario limpio: {diccionario}')

    #Eliminar el diccionario por completo
    del diccionario
    print(diccionario)

if __name__ == '__main__':
    main()