def main():

    edad_adulto = 18
    edad_persona = int (input('Proporciona tu edad: '))

    if edad_persona >= edad_adulto:
        print(f'La persona con edad {edad_persona} es una dulto')
    else:
        print(f'La persona con edad {edad_persona} es menor de edad')

    
if __name__=="__main__":
    main()