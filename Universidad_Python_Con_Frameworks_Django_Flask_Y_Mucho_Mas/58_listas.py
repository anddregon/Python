def main():
    #*Ponedemos tener listas con diferentes tipos de datos
    #*String, boleanos, enteros etc...

    #*Definimos una lista de tipo String
    nombres = ['Juan','Karla','Ricardo','María']
    
    print(f'Mi lista de nombres: {nombres}')
    
    #*Accedemos a los elementos de una lista
    print('\nAccedemos a elementos de la lista normalmente')
    print(f'[0] {nombres[0]}')
    print(f'[1] {nombres[1]}')

    #*Podemos acceder la lista de forma inversa
    print('\nAccedemos a elementos de la lista inversamente')
    print(f'[-1] {nombres[-1]}')
    print(f'[-2] {nombres[-2]}')


    print('\nOtras formas de acceder a elementos de lista:')
    #* Accedemos a los elementos del 0 al 2 sin incluir el indice 2
    #* es decir recuperamos el 0 y el 1
    print(f'[0:2] {nombres[0:2]}')

    #* Ir desde el inicio de la lista, acá recuperamos el 0,1,2 pues no incluye el 3
    print(f'[:3] {nombres[:3]}')

    #*Recorremos la lista desde el indice indicado hasta el final
    print(f'[1:] {nombres[1:]}')

    #*Del inicio al final de la lista:
    print(f'[::] {nombres[::]}')

    #*Cambiar valor
    print('\nCambiar valor: ')
    nombres[3] = 'Ivone'
    print(f'{nombres}')

    #*Iterar una lista:
    print('\nIteramos la lista:')
    #*La variable en singular y la lista en plural
    for nombre in nombres:
        print(nombre)
    else:
        print('NO existen más nombres en la lisa')







if __name__ == '__main__':
    main()