#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def has_duplicates(input_list):#Takes a list of numbers
    seen = set() # Keeps track of elements seen in the list.
    for item in input_list: #Starts a for loop 'the runs through each element in the input list
        if item in seen: #Inside the loop this line checks wether the current element is in the seen set 
            return True  # Found a duplicate
        seen.add(item) #Tracks elemnts already in seen set
    return False  # No duplicates found

my_list = [1, 2, 3, 2, 4, 5, 4, 6, 7, 7]
contains_duplicates = has_duplicates(my_list)

if contains_duplicates:
    print("The list contains duplicates.")
else:
    print("The list does not contain duplicates.")
    
