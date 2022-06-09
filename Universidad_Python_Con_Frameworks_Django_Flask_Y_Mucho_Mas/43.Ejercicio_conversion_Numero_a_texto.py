def main():

    numero = int(input('Proporciona un valor entre 1 y 3: '))

    #== es un operador de comparación
    #= es un operador de asignación
    #elif es "Sino Si"

    numeroTexto = ''
    if numero == 1:
        numeroTexto = 'Número uno'
    elif numero == 2:
        numeroTexto = 'Número dos'
    elif numero == 3:
        numeroTexto = 'Número tres'
    else:
        numeroTexto = 'Valor fuera de rango'

    print(f'Número proporcionado: {numero} - {numeroTexto}')
    
    
if __name__ == '__main__':
    main()