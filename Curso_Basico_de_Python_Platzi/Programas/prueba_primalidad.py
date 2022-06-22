# Funcion de Platzi
# def es_primo(numero):
#     contador = 0

#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else:
#         return False

# Función de John
# def es_primo(numero):
#     if numero == 1:
#         return False
#     elif numero == 2: #2 es el unico numero par que es primo
#         return True
#     else:
#         for i in range(2, numero):
#             if numero % i == 0:
#                 return False
            
#         return True

#Funcion principal (run)
# def run():
#     numero = int(input('Escribe un número: '))
#     if es_primo(numero):
#         print('Es primo')
#     else:
#         print('No es primo')



#SABER SI UN NUMERO ES PRIMO MEDIANTE TEOREMA DE WILSON
def factorial(n):
    fact = 1
    if n < 0:
        return 0
    elif n == 0:
        return 1
    while (n > 1):
        fact *= n #* fact = fact * n 
        n -= 1 #* n =
    return fact


def main():
    numero = int(input("Escoge un numero: "))
    wilson = factorial(numero - 1) + 1
    #print(wilson)
    if wilson % numero == 0:
        print("El numero es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    main()