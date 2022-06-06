#funcion principal
def main():
    num1 = int(input('Digite un numero: '))
    num2 = int(input('Digite un segundo numero: '))

    if num1 > num2:
        print(f'El numero mayor es: {num1}')
    else:
        print(f'El numero mayor es: {num2}')

        
#Entry Point o punto de entrada
if __name__ == '__main__':
    main()