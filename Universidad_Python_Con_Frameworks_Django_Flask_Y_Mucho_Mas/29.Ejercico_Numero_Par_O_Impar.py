def main():
    a = int(input('Escribe un valor entero: '))

    #Recordemos que == es el operador de comparación
    if a % 2 == 0:
        print(f'El valor de a: {a} es número par')
    else:
        print(f'El valor de a: {a} es número impar')

#*Entry Point
if __name__ == "__main__":
    main()
