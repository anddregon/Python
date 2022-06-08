def main():
    
    print('Proporciona los siguientes datos: ')

    nombre = input(f'Propociona el nombre del libro: ')
    id = input(f'Propociona el ID: ')
    precio = float(input('Propociona el precio: '))
    envio = input('Indica si el envio es gratuito (True/False): ')

    if envio == 'True':
        envio = True
    elif envio == 'False':
        envio = False
    else:
        envio= 'Valor incorrecto, debe escribir True/False'

    print(f'''
    Nombre: {nombre}
    id: {id}
    precio: {precio}
    envio: {envio}
    ''')

    


  
    

if __name__ == '__main__':
    main()