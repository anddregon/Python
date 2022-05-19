#Diccionario cuyas llaves son los 100 primeros numeros naturales y
#Cuyos valores son esos numeros elevados al cubo
#Aparte quiero guardar en las llaves los numeros que no sean divisibles
#por 3

import math

def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**2

    print('Diccionario 1: ')
    my_dict = {i: i**3 for i in range (1,101) if i % 3 != 0 }

    print(my_dict)

    #Dictionary comprehension cuyas llaves sean los 1000 primeros numeros
    #naturales con su raices cuadradas como valores

    print('Diccionario 2: ')

    my_dict2 = {i: math.sqrt(i) for i in range (1,1001)}
    print(my_dict2)

if __name__ == "__main__":
    run()