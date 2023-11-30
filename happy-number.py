#Write an algorithm to determine if a number n is happy.

#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.

 

def is_happy(n):  # Happy number is a number that will eventually equal 1 after a series of math operiation
    def get_next(num):
        # Function to calculate the sum of the squares of the digits of a number.
        total_sum = 0   #Keeps track of the cumulative sum of the number squared ( squares the number and adds the resuly)
        while num > 0:   #This is a while loop that contiunes as long as the number is greater than 0
            num, digit = divmod(num, 10) #This line does two things,divides "n" by 10 and returns two vaues, the quotient and reainder 
            total_sum += digit ** 2 #Take the digit separted from the number, squares it,and adds the reselt to the total sum
        return total_sum #Returns the value of the variable that contains the sum of the squared of the digits of the inputed number 

    seen = set() #Tracks numbers thats been encounted and detects cycles in the algorithum
    while n != 1 and n not in seen: #Main loop that contiunes as long as two conditions are met. First n is not equal to 1 and second n is not seen in set
        seen.add(n) #Adds current vaule of n to the seen set because number has been encountered 
        n = get_next(n) #Computes the sum of the squares of n digits and assigns result back to n. This step allows the algorthim to produce the next number in the sequence 

    return n == 1 #Checks if the vaule of n is equal to 1 or not 

# Example usage:
n = 19
result = is_happy(n) 
if result:
    print(f"{n} is a happy number.")
else:
    print(f"{n} is not a happy number.")

# True means it isa happy number and then the program prints " n is a happy number" and False if the number is not happy and then it prints " not a happy number?"