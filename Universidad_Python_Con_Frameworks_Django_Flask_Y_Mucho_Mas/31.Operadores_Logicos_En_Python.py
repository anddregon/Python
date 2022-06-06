def main():
    a = False
    b = True

    #Operador AND y OR son Binario pues necesitan 2 valores para ejecutarsen. 
    resultado = a and b 
    print(f'Operador Logico AND {resultado}')

    resultado = a or b
    print(f'Operador Logico OR {resultado}')

    #Operador NOT es Unario pues necesita 1 valor para ejecutarse
    resultado = not a
    print(f'Operador Logico NOT {resultado}')



if __name__ == '__main__':
    main()