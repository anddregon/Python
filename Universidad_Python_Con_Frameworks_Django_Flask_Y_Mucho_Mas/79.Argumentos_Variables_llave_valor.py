#* Si queremos pasar un diccionario es decir terminos
#* llave-valor utilizamos (**) al inicio del parametro de la función.
#* En la documentación de Python se utiliza (**kwargs) que se refiere
#* a elementos de llave valor pero podemos usar cualquier nombre

#* Si queremos tener argumentos variables, hacemos:

# def listar_elemtnos(nombre,*nombres, **terminos)

#* De esa forma podemos usar argumentos variables siendo *nombres una tupla
#* y **terminos un diccionario


def listar_terminos(**terminos):

    #* Iteramos el diccionario recibido

    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

def main():

    listar_terminos(IDE='Integrated Development Environment', PK = 'Primary Key')
    listar_terminos(DBMS = 'Database Managemnt System')



if __name__ == '__main__':
    main()
