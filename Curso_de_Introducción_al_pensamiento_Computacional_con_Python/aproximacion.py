def run():
    #Numero al que se le calculará la raiz cuadrada
    objetivo = int(input('Escoge un número: '))

    #Margen de error para encontrar esa raiz cuadrada
    epsilon = 0.01 # %1

    #valor que se irá sumando secuanecialmente hasta encontrara la raiz cuadrada
    paso = epsilon**2

    #Se comenzará a buscar a la raiz cuadrada desde 0.0 en adelante
    respuesta = 0.0
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print (f'No se encontró la raiz cuadrada {objetivo}')
    else: print(f'La raiz cuadrada de {objetivo} es {respuesta}')


if __name__ == '__main__':
    run()
     





