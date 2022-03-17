def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print("llave 1 del diccionario: ")
    # print(mi_diccionario['llave1'])
    # print("llave 2 del diccionario: ") 
    # print(mi_diccionario['llave2'])
    # print("llave 3 del diccionario: ")
    # print(mi_diccionario['llave3'])
    
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }

    
    #print(poblacion_paises['Argentina'])
    
    #*Recorrer diccionario y mostrar sus llaves (keys) mediante el metodo keys
    # for pais in poblacion_paises.keys():
    #      print("Key: ")  
    #     print(pais)
    
    #*Recorrer diccionario y mostrar sus valores (values) mediante el metodo values  
    # for pais in poblacion_paises.values():
    #     print("valor: ")
    #     print(pais)
    
    
    #*Recorrer diccionario y mostrar sus valores y las llaves con metodo items
    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")
            

if __name__ == '__main__':
    run()