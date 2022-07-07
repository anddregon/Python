#Anteponemos * porque no sabemos cantidad de nombres a recibir
#*De manera interna Python lo convierte a una tupla, la tupla args
#*Poner args es una buena practica para recibir valores variables

def multiplicar_valores(*args):
    resultado = 1
    for numero in args:
        #resultado = resultado * numero
        resultado *= numero
    return resultado   
        
def main():

    print(multiplicar_valores(5,5,5,2))

if __name__ == '__main__':

    main()