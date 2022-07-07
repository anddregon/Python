#def sumar (a = 3, b = 3) -> int: #*-> int es un indicio de lo que puede devolver
                                   #* esa funcion pero no es obligatorio


def sumar (a = 3, b = 3):
               
        return a + b


def main():

    #*Acá se toman los valores por default de los parametros que serían 3,3
    print(f'Resultado sumar: {sumar()}')

    #*Acá se sobreescribe los valores de los parametros por 5,5
    print(f'Resultado sumar: {sumar(5,5)}')


if __name__ == '__main__':
    main()
