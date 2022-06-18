def main():

    #*Sintaxis de range: 
    #* (inicio<opcional>, fin<requerido>, incremento<opcional>)

    #*Iterar un rango del 0 a 10 e imprimir números divisibles entre 3
    print('Números divisibles entre 3 del 0 al 10: ')
    for i in range (11):
        if i % 3 == 0:
            print(i)

    #*Crear un rango de números de 2 a 6 e imprimirlos
    print('Rango de números del 2 al 6: ')
    for i in range (2,7):
        print(i)

    #*Crear un rango de 3 a 10, pero con incremento de 2 en 2
    print('Rango de números del 3 al 10 con incremento de 2 en 2: ')
    for i in range (3,11,2):
        print(i)


if __name__ == '__main__':
    main()