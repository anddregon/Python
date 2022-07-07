#Anteponemos * porque no sabemos cantidad de nombres a recibir
#*De manera interna Python lo convierte a una tupla, la tupla nombres
#*Poner args es una buena practica para recibir valores variables

def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)  
    print(f'Tipo de dato de nombres: {type(nombres)}')

def main():
#*No sabemos la cantidad de valores a pasar
    listar_nombres('Wilson','Gigi','S4vitar','Chema')
    listar_nombres('Alexa', 'Ria', 'Nya','Paige', 'Becky')
  


if __name__ == '__main__':
    main()