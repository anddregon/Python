def main():
    edad = int(input('Proporciona tu edad: '))
    if edad >= 0 and edad <= 10:
        print('La infancia es increible')
    elif edad >= 10 and edad <= 20:
        print('Muchos cambios y mucho estudio')
    elif edad >= 20 and edad <= 30:
        print('Amor y comienza el trabajo')
    else:
        print('Etapa de vida no reconocida')    

if __name__ == '__main__':
    main()