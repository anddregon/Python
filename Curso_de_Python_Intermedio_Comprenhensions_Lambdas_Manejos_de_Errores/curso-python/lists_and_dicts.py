#Main fuction
def main():
    my_list = [1,'Hello', True, 4.5 ]
    my_dict = {'firstname': 'Facundo', 'lastaname': 'García'}

    #* This is a list of dictionaries, we got 5 elements (dictionaries) on this list
    super_list = [
        {'firstname': 'Facundo', 'lastaname': 'García'},
        {'firstname': 'Miguel', 'lastaname': 'Torres'},
        {'firstname': 'Pepe', 'lastaname': 'Rodelo'},
        {'firstname': 'Susana', 'lastaname': 'Materinez'},
        {'firstname': 'Jose', 'lastaname': 'García'},
    ]

    #* This is a dictionary of lists
    #* We create a key and then we asign a value to it
    # * that value is a list  
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums" : [-1, -2, 0, 1, 2],
        "floating_nums" : [1.1, 4.5, 6.43],
    }

    
    print('This is a list of dictionaries 📚')
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

    #* Now we use the "items" method to 
    #* loop through the key and value of a dictionary
    #* at the same time.
    print('\nThis is a dictionary of lists 📓')
    for key, value in super_dict.items():
        print(key, "-", value)
    
    
        
#Entry Point
if __name__ == '__main__':
    main()


