def main():
    #* Las tuplas son estructuras de datos no mutables
             
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

    



if __name__ == '__main__':
    main()