def enumeracion(objetivo):
    
respuesta = 0
    
while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
        
if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aproximacion(objetivo):
    
    epsilon = 0.01 # %1

paso = epsilon**2

    respuesta = 0.0
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print (f'No se encontró la raiz cuadrada {objetivo}')
    else: print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria(objetivo):
    
    
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def main():
    
    menu = """
    Bienvenido al programa para calcular raices cuadradas 🧮
    Elija el algorimo para hacer el calculo:
    1. Enumeración exhaustiva
    2. Aproximación de soluciones
    3. Busqueda Binaria
    """
    opcion = int(input (menu))
    
    objetivo = int(input('Digita un número entero: '))

    if opcion == 1:
        enumeracion(objetivo)
    elif opcion == 2:
        aproximacion(objetivo)
    elif opcion == 3:
        busqueda_binaria(objetivo)
    else:
        print("Ingresa una opción correcta por favor")
    
if __name__ == '__main__':
    main()