#Función principal de toda la vida (buena practica)
def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname':'Facundo', 'lastname':'García'}

#* Esta es una lista de diccionarios
    super_list = [
        {'firstname':'Facundo', 'lastname':'García'},
        {'firstname':'Miguel', 'lastname':'Torres'},
        {'firstname':'Pepe', 'lastname':'Rodelo'},
        {'firstname':'Susana', 'lastname':'Martinez'},
        {'firstname':'Jose', 'lastname':'García'},
    ]

#* Este es un diccionario de listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, -3, -4, -5],
        "floating_nums": [1.1, 4.5, 6.43],
    }

#! Imprimimos el diccionario de listas
#*El metodo items nos permite recorrer las llaves y valores al mismo tiempo
#*de un diccionario con un ciclo
    print('Diccionario de listas')
    for key, value in super_dict.items():
        print(f'{key} - {value}')

#! Imprimimos la lista de diccionarios
    print('\nLista de diccionarios')
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')
            
#Entry Point de toda la vida (buena practica)
if __name__ == '__main__':
    main()

















