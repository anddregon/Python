def suma (num1, num2):

    return num1 + num2

def main():
    num1 = int(input('Digite un número: '))
    num2 = int(input('Digite un segundo número: '))
    print(f'El resultado de la suma es: {suma(num1,num2)}')

if __name__ == '__main__':
    main()