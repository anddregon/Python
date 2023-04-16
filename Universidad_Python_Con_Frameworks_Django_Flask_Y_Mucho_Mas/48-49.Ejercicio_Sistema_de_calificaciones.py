def main():
    
    calificacion = int(input('Digite una calificación del 1 al 10 : '))

    # if numero >= 9 and numero <= 10:
    #     print('Su calificacioón es: A ')

    # elif numero >= 8 and numero < 9:
    #     print('Su calificación es: B ')

    # elif numero >= 7 and numero < 8:
    #     print('Su calificación es: C ')

    # elif numero >= 6 and numero < 7:
    #     print('Su calificación es: D ')
    
    # elif numero >= 0 and numero < 6:
    #     print('Su calificación es: F ')

    # else:
    #     print('Valor desconocido')

    #*Vamos a hacerlo con la sintaxis simplificada del operador AND
    #*Se lee: Si la calificación es mayor o igual que 9 Y y la calificacion es
    #* menor o igual que 10

    if  9 <= calificacion <= 10:
        print('Su calificacioón es: A ')
    
    elif 8 <= calificacion < 9:
        print('Su calificación es: B ')
    
    elif 7 <= calificacion < 8:
        print('Su calificación es: C ')
    
    elif 6 <= calificacion < 7:
        print('Su calificación es: D ')
    
    elif 0 <= calificacion < 6:
        print('Su calificación es: F ')
    else:
        print('Valor incorrecto')


if __name__ == '__main__':
    main()