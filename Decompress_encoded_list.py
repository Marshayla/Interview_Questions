#We are given a list nums of integers representing a list compressed with run-length encoding.

#Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

#Return the decompressed list.

def decompress(nums): #This line defines a function named 'decompress' that takes a list 'nums' as input 
    result = [] 
    for i in range(0, len(nums), 2):#Starts a 'for' loop that iterates thrpugh the input list 'nums' with a step of 2. Insures that 'i' and 'i+i' respesents adjacent pairs.
        freq, val = nums[i], nums[i + 1] #Takes two vaules from the list 'nums' at positions 'i' and 'i+i' and assigns the first value to 'freg' and the second value to 'val'
        result.extend([val] * freq) #Extends the 'result' list by repeating the value 'val' 'freg' times
    return result #Returns the decompressed list stored in the 'result' variable 

# Example usage:
compressed_list = [3, 1, 4, 2, 2, 5, 1, 7]
decompressed_result = decompress(compressed_list)
print(decompressed_result)
