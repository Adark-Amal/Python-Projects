def generate_acronym(sentence: str) -> str:
    """
    Function that generates the acronym for a given sentence
    
    Parameters:
        sentence (str): The sentence for which the acronym needs to be generated
        
    Returns:
        acronym (str): The generated acronym
    """
    
    # convert to lowercase
    sentence = sentence.lower()
    
    # Split the sentence into a list of words
    words = sentence.split()

    # Initialize an empty string to store the acronym
    acronym = ""

    # Generate the acronym by selecting the first letters of each word and capitalizing them
    for word in words:
        acronym += word[0].upper()

    # Return the generated acronym
    return acronym


# Prompt the user to enter a sentence
user_input = input("Please enter a sentence: ")

# Generate the acronym for the input sentence
result = generate_acronym(user_input)

# Display the generated acronym
print("Acronym: {}".format(result))
