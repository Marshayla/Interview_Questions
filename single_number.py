def singleNumber(nums): #Defines that single number takes a list of intergers "num" as an imput 
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space.


 def singleNumber(nums):#Takes a list of intergers "nums" as an input
    result = 0 #Keeps track of the number that only appears once in the list 
    for num in nums: #Starts a "for" loop that runs through each element in the list "nums"
        result ^= num #Updating the result by mixing it with the vaule of num
    return result #
# Example usage:
nums = [4, 1, 2, 1, 2]
single = singleNumber(nums)
print(single)  # Output: 4

#This code anazles an array of numbers and pulls out the number that only appears once.
# A for loop is a controlled flow that is used to repeately run through a sequence of elemnts, like a list,array or a range of numbers. 
