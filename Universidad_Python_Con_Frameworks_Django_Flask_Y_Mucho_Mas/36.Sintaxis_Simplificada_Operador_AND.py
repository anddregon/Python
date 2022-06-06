def main():
    edad = int(input('Introduce tu edad: '))

#veintes = edad >= 20 and edad < 30
#print(veintes)
#treintas = edad >= 30 and edad <40
#print(treintas)

#Esto se lee: si la edad es mayor o igual que 20 y la edad es menor que 30.
#O si la edad es mayor o igual que 30 y la edad es menor que 40.
#Es lo mismo que lo de arriba solo que simplificado y sin el operador and.

    if ( 20 <= edad < 30) or (30 <= edad <40):
        print('Dentro de rango (20\'s) o (30\'s)')
#    if veintes:
#        print('Dentro de los 20\'s')
#    elif treintas:
#        print('Dentro de los 30\'s')
#    else:
#        print('Fuera de rango')
    else:
        print("No está dentro de los 20's ni 30's")

if __name__ == '__main__':
    main()