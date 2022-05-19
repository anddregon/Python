def run():
    # squares = []

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)



    #* List Comprenhension: Para cada i en el rango que va de 1 a
    #* 101 guerde esa i al cuadrado solo si esa i modulo 3 es 
    #* diferente de cero.

    #*En otras palabras: Para cada i de los numeros del 1 al 101
    #*guarde esa i al cuadrado solo si no es divisible por 3 
    
 
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    print(squares)

    #?Ahora este es un List Comprehension de todos los multiplos de 4
    #? que a la vez tambien son multiplos de 6 y 9, hasta 5 digitos.

    multiples = [ i for i in range(1, 100000) if i % 36 == 0]
    print (multiples)

    #?Ahí usamos el 36 porque es el unico numero multiplo de los
    #?tres numeros (4,6 y 9) al mismo tiempo

if __name__ == "__main__":
    run()