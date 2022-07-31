def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)


def main():
    nombres = ['Juan' , 'Carla' , 'Guillermo']
    desplegar_nombres(nombres) #Enviamos una lista
    desplegar_nombres('Carlos') #Enviamos un String
    desplegar_nombres((10,11)) #Enviamos una tupla
    desplegar_nombres([12,13]) #Enviamos otra lista

if __name__ == '__main__':
    main()