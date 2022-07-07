#Anteponemos * porque no sabemos cantidad de nombres a recibir
#*De manera interna Python lo convierte a una tupla, la tupla args
#*Poner args es una buena practica para recibir valores variables


def restar_valores(*args):
    resultado = 0
    for numero in args:
        #resultado = resultado - numero
        resultado -= numero
    return resultado   

def main():
    print(restar_valores(100,50))

if __name__ == '__main__':
    main()