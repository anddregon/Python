def main():
    mes = int(input('Proporciona mes del año (1-12): '))

    #*le asignacmos el valor None a la variable, este es el equivalente
    #*a null en java

    estacion = None
    #Recordemos que == es operador de comparación
    if mes == 1 or mes == 2 or mes == 12:
        estacion = 'Invierno'

    elif mes == 3 or mes == 4 or mes == 5:
        estacion = 'Primavera'

    elif mes == 6 or mes == 7 or mes == 8:
        estacion = 'Verano'

    elif mes == 9 or mes == 10 or mes == 11:
        estacion = 'Otoño'

    else:
        estacion = 'Mes incorrecto'

    print(f'Para el mes {mes} la estación es: {estacion}')
 

if __name__ == '__main__':
    main()