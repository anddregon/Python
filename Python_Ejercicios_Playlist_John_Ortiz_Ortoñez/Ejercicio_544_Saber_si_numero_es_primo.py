# Ejercicio 544: Crear una funcón para saber si un número es primo

def es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2: #2 es el unico numero par que es primo
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
            
        return True
     
     
     
for i in range (1, 100+1):
    print (i, es_primo(i))

        
    
    