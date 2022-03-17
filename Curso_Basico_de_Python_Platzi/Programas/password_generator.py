import random

#! Reminder: All my code must always be in English

def generate_password():
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']
    
    symbols = ['!', '#', '$', '&', '/', '(', ')', '=',
                    '?', '.', ',', '_', '-', '*', '}', '{', 
                    '[', ']']
    
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    characters = capital_letters + lowercase + symbols + numbers
    
    #listas vacia
    password = []
    
    #Quiero la contraseña de 15 caracteres
    for i in range(15):
        #we use the choice function of the random module 
        character_random = random.choice(characters)
        password.append(character_random)
        
    #* Convert list to string    
    password = "".join(password)
    return password
        

#main function
def run():
    password = generate_password()
    print("Your new password is: " + password)


#Entry point
if __name__ == '__main__':
    run()
    