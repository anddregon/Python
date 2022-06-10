def main():
    condicion = True

    # if condicion:
    #     print('Condicion verdadera')

    # else:
    #     print('Condicion falsa')


    #*Si la condición es verdadera se ejecuta la parte izquierda
    #*si es falsa se ejectua la parte derecha

    #*Se recomienda esta sintaxis simplificada cuando el codigo es muy pequeño
    #*en esta sintaxis simplificada no se puede agregar elif
    #*si tenemos mas lineas de codigo se recomienda como siempre
    print('Condicion verdadera') if condicion else print ('Condicion falsa')

if __name__=='__main__':
    main()