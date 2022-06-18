def main():
    x = 10
    y = 2
    z = x + y
    #* I use f-strings to format strings, this is a new feature
    #* available since Python 3.6

    #*Una literal es un valor que le asignamos a una variable
    #*Las literales se almacenan en una direccion en memoria RAM
    #*Literal 10 se almacena en una direccion en memoria 
    #*Literal 2 se almacena en otra direccion en memoria
    #*Las variables son las encargadas de apuntar a esa direccion en memoria
    #*Con la función ID podemos obtener la direccion en memoria a la cual
    #*apuntan las variables o en la que están ubicadas las literales
    #*ID es una built in function https://docs.python.org/3/library/functions.html
    #* Direcciones en memoria son usualmente en hexadecimal
    #* Es normal que al volver a ejectuar el programa, cambien las direcciones en
    #* memoria RAM pues recordemos que la memoria RAm es volatil

    print(f'this is the literal or the value of the variable: {x}')
    print(f'this is the literal or the value of the variable: {y}')
    print(f'this is the literal or the value of the variable: {z}')
    
    print(f'this is de memory address of the value of the variable x: ')
    print(id(x))
    print(f'this is de memory address of the value of the variable y: ')
    print(id(y))
    
    print(f'this is de memory address of the value of the variable z: ')
    print(id(z))


if __name__ == '__main__':
    main()
    