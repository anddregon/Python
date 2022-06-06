def main():

    vacaciones = True
    dia_descanso = True

    #invertimos la logica en nuestro algoritmo usando el operador NOT    
    if not (vacaciones or dia_descanso):
        print('Tiene deberes por hacer')     
    else:
        print('Puede asistir al juego de su hijo')    
       
if __name__=='__main__':
    main()