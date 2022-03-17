def main():
    x = 10
    y = 2
    z = x + y
    #* I use f-strings to format strings, this is a new feature
    #* available since Python 3.6
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
    