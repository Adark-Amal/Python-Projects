import random
import string

# NB: This is the revised version of the password_generator_old code

def password_generator():
    """
    Function to generate a random password based on user input
    
    Parameters:
        None
    
    Returns:
        None: Only prints the generated password
    """
    
    # Prompt the user to enter the desired length of the password
    length = int(input("Enter the length of the password: "))

    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Print the generated password
    print("Generated Password:", password)


# Run the password generator function
password_generator()
