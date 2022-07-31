#Funcion recursiva la cual se llama a si mismav
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

def main():

    numero = int(input('Digita un número: '))
    print(f'El factorial del número {numero} es: {factorial(numero)}')

if __name__ == '__main__':
    main()