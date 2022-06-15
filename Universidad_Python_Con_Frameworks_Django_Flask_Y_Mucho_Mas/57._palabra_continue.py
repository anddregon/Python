def main():
    
    # for i in range(6):
    #     if i % 2 == 0:
    #         print(f'Numero par: {i}')

    for i in range (6):
        #* Si el valor de i no es divisible entre 2 nos vamos a la siguiente
        #* iteración
        if i % 2 != 0:
            #*continue a diferencia de break ejecuta la siguente iteración
            #* el continue está diciendo "siga iterando"
            continue
        print(f'Valor: {i}')



if __name__ == '__main__':
    main()
    




