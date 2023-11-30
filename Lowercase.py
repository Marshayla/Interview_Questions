# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

def replace_uppercase_with_lowercase(s): #Defines a function named replace_uppercase_with_lowercase and takes a string 's' as input
    result = "" #Initializes an empty string called 'result' and store the final string with all uppercase letters replaced by thier lowercase equivialents
    for char in s: #Starts a 'for' loop that iterates over each character in the inputed string 
        result += char.lower() #Inside the loop,for each character, its lowercase version is appended to the 'result' string 
    return result #Function returns the modified string stored in the 'result' variable

# Example usage:
input_string = "Hello World"
result = replace_uppercase_with_lowercase(input_string)
print(result)
