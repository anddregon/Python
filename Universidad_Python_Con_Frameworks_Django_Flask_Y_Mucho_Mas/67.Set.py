#* Estructura de datos Set: 
#* -> No mantiene un orden
#* -> No permite almacenar elementos duplicados
#* -> No se puede modificar elementos
#* -> Si es posible agregar/eliminar eleminiarlos 
#* -> Se representan con {}

def main():
    
    planetas = {'Marte','Jupiter','Saturno'}
    print(f'Set: {planetas}')

    #largo
    print(f'Número de elementos en el Set: {len(planetas)}')

    #Revisar si un elemento está presente
    #Esta misma pregunta la podemos hacer con Listas y Tuplas
    print('Marte' in planetas)

    #Agregar un elemento
    planetas.add('Tierra')
    print(planetas)

    #Set no soporta elementos duplicados, muy util para cuando no queramos
    #duplicar elementos
    planetas.add('Tierra')
    print(planetas)

    #Eliminar elemento
    planetas.remove('Tierra')
    print(planetas)

    #Discard tambien es para eliminar elemento pero sin tirar error sino
    #se encuentra dicho elemento
    planetas.discard('Jupiter')
    print(planetas)

    #Limpiar Set
    planetas.clear()
    print(planetas)

    #Eliminar por completo set
    del planetas
    print(planetas)
    


if __name__ == '__main__':
    main()