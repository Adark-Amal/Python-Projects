def character_counter(text: str) -> dict:
    """
    Function that counts the occurrences of each character in a given text
    
    Parameters:
        text (str): The input text to count the character occurrences from
    
    Returns:
        count_dict (dict): A dictionary containing the counts of each character
    """

    count_dict = {}

    # Loop through text and check existence of character
    for char in text:
        count_dict[char] = count_dict.get(char, 0) + 1

    return count_dict

# take input from user
user_input = input("Enter text here: ")

# call the character counter function
counter = character_counter(user_input)

# print the generated dictionary
print(counter)
