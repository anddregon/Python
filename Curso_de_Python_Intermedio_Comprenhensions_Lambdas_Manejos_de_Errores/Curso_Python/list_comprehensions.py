def main():
    # squares = []
    # for i in range (1, 101):
    #     if i % 3 != 0: #Cuadrado de lo #'s que no son divisbles entre 3
    #         squares.append(i**2)
    squares = [i**2 for i in range (1, 101) if i % 3 != 0]

    print(squares)

if __name__ == '__main__':
    main()
