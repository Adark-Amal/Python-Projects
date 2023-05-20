import random
    
def password_generator():
    """
    Function to generate a random password based on user input

    Parameters:
        None

    Returns:
        None: Only prints the generated password
    """

    # take user input for length of password
    password_length = int(input("Enter the length of password: "))
    
    # characters to generate password from
    characters ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    # randomly generate the password and print results
    password = "".join(random.sample(characters, password_length))

    # Print the generated password
    print("Generated Password:", password)
    
    
# call the password function
password_generator()