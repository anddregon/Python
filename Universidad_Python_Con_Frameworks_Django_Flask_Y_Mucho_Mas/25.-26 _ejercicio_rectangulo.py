#Calcular area y perimetro de un rectangulo

def calcular_area(alto,ancho):
    return(alto*ancho) 

def calcular_perimetro(alto,ancho):
    return((alto+ancho)*2)
     
#Función principal
def main():
    alto = int(input('Digite el alto del rectangulo: '))
    ancho = int(input ('Digite el ancho del rectangulo: '))
    print(f'El area del rectangulo es: {calcular_area(alto,ancho)}')
    print(f'El perimetro del rectangulo es: {calcular_perimetro(alto,ancho)}')

    
#*Entry Point
if __name__ == "__main__":
    main()
