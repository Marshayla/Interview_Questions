#Given a string s consisting of words and spaces, return the length of the last word in the string.

#A word is a maximal 
#substring
# consisting of non-space characters only.

def length_of_last_word(s): # Takes a single argument 's' which is expected to a string
    stripped = s.strip()  # Remove leading and trailing spaces so they it doesnt affect the calculations
    strList = stripped.split()  # Split the stripped string into words and stores the result in the variable 'strlist'
    if not strList:
        return 0  # If there are no words in the list, return 0
    lastWord = strList[-1]  # Get the last word in the list
    return len(lastWord)  # Return the length of the last word

# Example usage:
input_string = "Hello World"
result = length_of_last_word(input_string)
print(f"The length of the last word is: {result}")
