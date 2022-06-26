def main():
    #* ->Las tuplas son estructuras de datos no mutables
    #* -> Se representan con ()
             
    frutas = ('Naranja', 'Platano', 'Guayaba')

    print(f'Tupla frutas: {frutas}')    

    #* Saber el largo de un tupla
    print(f'Numero de elementos en la tupla: {len(frutas)}')

    #*Acceder elemento
    print(f'Indice [0]: {frutas[0]}')

    #*Navegación inversa
    print(f'Indice [-1]: {frutas[-1]}')

    #*Acceder a rango de valores (el ultimo indice no se incluye)
    print(f'Rango [0:1]: {frutas[0:1]}')

    #* Recorrer elementos
    for fruta in frutas:
        print(fruta, end=' ')

    #*Cambiar valor tupla
    # frutas[0] = 'Pera'
    #convertimos tupla frutas en una lista
    frutas_lista = list(frutas)
    frutas_lista [0] = 'Pera'
    #convertimos lista frutas_lista en una tupla
    frutas = tuple(frutas_lista)
    print('\n',frutas)

    #*Eliminar tupla por completo
    del frutas

    #!Utilizaremos una lista cuando consideremos que vamos a cambiar elementos
    #!en un futuro, y una tupla cuando estemos seguros de que no vamos a cambiar
    #!sus elementos

    
if __name__ == '__main__':
    main()