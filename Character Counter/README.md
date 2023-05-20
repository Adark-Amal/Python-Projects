## Character Occurrence Counter

### About Project

The Character Occurrence Counter is a Python program that counts the occurrences of each character in a given string. By implementing an algorithm that iterates through the string and stores the occurrence of each character in a dictionary, the code returns the count of each character in the input string.

### Problem Statement

The project aims to solve the problem of counting the occurrences of characters in a string without using any external libraries. By implementing the algorithm, users can determine the number of times each character appears in a given text.

### Algorithm

The algorithm used in the Character Occurrence Counter is as follows:

1. Create an empty dictionary to store the occurrence of each character.
2. Iterate through each character in the input text.
3. Check if the character is already a key in the dictionary. If it is, increment the count by 1. If it is not, add the character as a key with an initial count of 1.
   - Alternatively, the `get()` method can be used to achieve the same result without an explicit if/else block.
4. Print the resulting dictionary containing the counts of each character.

### Python Skills Learned

During the development of this project, the following Python skills were utilized:

- Looping through characters in a string.
- Working with dictionaries: adding and updating key-value pairs.
- String manipulation: accessing individual characters.

### Installation

To run the Character Occurrence Counter program, no additional libraries are required. Simply clone the repository or download the source code file.

### Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the Character Occurrence Counter:
```python
    python character_counter.py
```

4. Enter the text for which you want to count the character occurrences.
5. The program will print a dictionary containing the counts of each character in the input text.

