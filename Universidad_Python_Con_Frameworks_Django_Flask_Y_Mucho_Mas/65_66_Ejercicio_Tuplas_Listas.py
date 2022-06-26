#Dada una tupla:
#*Crear una lista que solo incluya los numeros menores a 5


def main():
    #*Mi solución
    #tupla_de_numeros = (13, 1, 8, 3, 2, 5, 8)
    # print(f'Tupla de números: {tupla_de_numeros}')
    # lista_de_numeros = list(tupla_de_numeros)
    # print(f'Lista de números: {lista_de_numeros}')
    # lista_de_numeros_2 = []
    # for numero in lista_de_numeros:
    #     if numero < 5:
    #         lista_de_numeros_2.append(numero)
    #     else:
    #         continue
    
    # print(f'Lista con numeros menores a 5: {lista_de_numeros_2}')

    #*Solución de Ubaldo
    tupla = (13, 1, 8, 3, 2, 5, 8)
    lista = []
    for elemento in tupla:
        if elemento < 5: 
            lista.append(elemento) #usamos el metodo de listas append
    print(f'Nueva lista: {lista}')

   
if __name__ == '__main__':
    main()