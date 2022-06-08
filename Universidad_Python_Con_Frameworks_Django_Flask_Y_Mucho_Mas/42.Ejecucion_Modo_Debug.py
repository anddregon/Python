def main():
#222222222222222    
    
#Si en la condicion el valor es distinto de vacio guarda un True, por
#ejemplo si introducimos un numero.

#Si en la condicion el valor es una cadena vacia, ahí si se guarda 
#un False

#Eso anterior es en caso de que solo pongamos if condicion: sin el == True
    
#* Video: https://www.youtube.com/watch?v=xAG1FBEIf3g&t=108s
#* Debug es un proceso informatico que se encarga de eliminar 
#* errores, para ello en VScode tenemos diferentes herramientas.

#* Para ello le damos en Run and debug en la mariquita del lado
#* izquierdo/Run and Debug/marcamos un BreakPoint, y ya podemos jugar
#* con el Step over, Step Into y demás... y si le damos click derecho
#* en el break Point/Edit Break Point podemos crear Expressions, Hit
#* Count y Log Messages

    
    condicion = input('Digite True o False: ')
    

    if condicion == 'True' or condicion == 'true':
        print('Condicion verdadera')
                   
    elif condicion == 'False' or condicion == 'false':
        print ('Condición Falsa')

    else:
        print('Condicion no reconocida')


if __name__ == '__main__':
    main()
