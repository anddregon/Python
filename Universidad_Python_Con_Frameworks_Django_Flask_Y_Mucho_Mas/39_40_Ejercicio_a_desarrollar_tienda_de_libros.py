def main():
    
    print('Proporciona los siguientes datos: ')

    nombre = input(f'Propociona el nombre:')
    id = input(f'Propociona el ID:')
    precio = input('Propociona el precio:')
    envio = input('Indica si el envio es gratuito (True/False): ')

    print(f'Nombre del libro: {nombre}\nID: {id}\nPrecio: {precio}\nEnvio {envio}')

  
    

if __name__ == '__main__':
    main