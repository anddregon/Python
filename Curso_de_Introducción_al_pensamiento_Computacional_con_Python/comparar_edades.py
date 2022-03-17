 #* Programa para comparar edades de 2 usuarios con nombre
 #* y diga quien es mayor de los 2
 
def run():
    print('**Bienvenido usuario 1**')
    nombre_1 = input('Por favor digite su nombre : ' )
    edad_1 = int (input('Por favor digite su edad : ' ))
    
    print('**Bienvenido usuario 2**')
    nombre_2 = input('Por favor digite su nombre : ' )
    edad_2 = int (input('Por favor digite su edad : ' ))
        
    if edad_1 > edad_2:
        edad_1 = str(edad_1)
        edad_2 = str(edad_2)
        print ('La edad de ' + nombre_1 + ' es mayor que la edad de ' + nombre_2)
    elif edad_1 < edad_2:
        print('La edad de ' + nombre_1 + ' es menor que la edad de ' + nombre_2)
    else:
        print('Las dos edades son igules')        

if __name__ == '__main__':
    run()
     