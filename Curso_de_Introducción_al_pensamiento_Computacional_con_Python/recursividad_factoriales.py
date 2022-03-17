def factorial(n):
    """ Calcula el factorial de n.

    n int > 0
    return n!
    """
    print(n)
    if n == 1:
        return 1

    return n * factorial(n-1)

#Función principal
def main():
    n = int(input('Escribe un entero: '))
    #print('Este es el resultado' + str (factorial(n)))
    print(f'Este es el resultado: {factorial(n)}')

#Entry Point o punto de entrada
if __name__ == '__main__':
    main()
