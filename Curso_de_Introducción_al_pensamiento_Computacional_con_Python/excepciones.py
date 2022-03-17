def divide_elementos_de_lista(lista, divisor):

        #Hacemos programación defensiva con try except

    try:        
    
        return [i / divisor for i in lista]
    
    #En la variable e guardamos el mensaje de error
    except ZeroDivisionError as e: 
        print(e)
        return lista
        #Retornamos la lista original si alguien pone cero
        #en el divisor manejando así la expceción sin 
        #romper el programa

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))
