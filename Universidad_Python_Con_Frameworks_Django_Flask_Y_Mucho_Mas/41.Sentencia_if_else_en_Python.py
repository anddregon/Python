#Operador de asignación =
#Operador de comparación ==
def main():
#Si en la condicion el valor es distinto de vacio guarda un True, por
#ejemplo si introducimos un numero.

#Si en la condicion el valor es una cadena vacia, ahí si se guarda 
#un False

#Eso anterior es en caso de que solo pongamos if condicion: sin el == True
    condicion = input('Digite True o False: ')
    

    if condicion == 'True' or condicion == 'true':
        print('Condicion verdadera')
                   
    elif condicion == 'False' or condicion == 'false':
        print ('Condición Falsa')

    else:
        print('Condicion no reconocida')


if __name__ == '__main__':
    main()