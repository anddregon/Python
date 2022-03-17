#* Programa para determinar si un numero tiene una raiz cuadrada exacta

def main():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0
    
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
        
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
        

if __name__ == '__main__':
    main()
    


