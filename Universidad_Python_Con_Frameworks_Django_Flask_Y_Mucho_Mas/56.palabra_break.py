def main():
    #Operador de comparación ==
    for letra in 'Holanda':
        if letra == 'a':
            print(f'Letra encontrada: {letra}')
            break #rompe todo el ciclo incluyendo el else
            #El break es util cuando estamos buscando un elemento
            #dentro de una lista de datosy una vez encontrado ese
            #elemento usamos Break para romper el ciclo
    else:
        print('Fin ciclo for')

if __name__ == '__main__':
    main()