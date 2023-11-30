#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
#If the two linked lists have no intersection at all, return null.

class ListNode: # Creates linked list nodes. Each node has a 'Val" to store theb vaule and a 'next' to point to the nect node in the list
    def __init__(self, value):
        self.val = value
        self.next = None

def getIntersectionNode(headA, headB): #This function takes two linked list as inputs and return node at which the two list intersect or 'none' if theres no intersection
    # Calculate the lengths of the two linked lists
    lenA, lenB = 0, 0
    nodeA, nodeB = headA, headB

    while nodeA: #Starts a while loop that continues to iterate as long as 'nodeA' is not 'none'
        lenA += 1 #Inside loop , the variable 'lenA' is incremented by 1.This variable is used to keep track of length of the linked list.
        nodeA = nodeA.next #Moves the 'nodeA' pointer to the next node in the linked list by assigning it the vaule of 'nodeA.next'. This is how you transversethe linked list ,moving from one node to the next.

    while nodeB: #Starts a while loop to continue to iterate as long 'nodeB' is not 'none' 
        lenB += 1 #LenB is incremented by 1 and used to keep track of length of thee linked list pointed 
        nodeB = nodeB.next #Moves 'nodeB' pointer to the next node in the linked list by assigning it the vaule of 'nodeB.next' 

    # Reset the pointers to the head of the lists
    nodeA, nodeB = headA, headB #Assigns the vaules of 'headA' and 'headB' to the variables 'nodeA' and 'nodeB'

    # Move the longer list's pointer to match the length of the shorter list
    if lenA > lenB: #This condition checks the length of the linked list 'A' is greater than the length of the link list 'B', and advances the pointer 'nodeA' by the differnece 
        for _ in range(lenA - lenB): #'For' loop that runs through the number of times equal to the differnce in lengths between linked list 'A' and 'B' and advances tghe pointer 'nodeA' by the differnce
            nodeA = nodeA.next #Moves 'nodeA' to the next node in the list 
    elif lenB > lenA: #This condition checks the length of the linked list 'B' is greater than 'A'. If true, it means linked list 'B' is longer than 'A'
        for _ in range(lenB - lenA): #Runs the number of times equal to the differnce in lengths between linked list 'B' and 'A'. Advances the pointer 'nodeB'by the difference. 
            nodeB = nodeB.next #Moves 'nodeB' to the next node in the list 

    # Traverse both lists together until they intersect
    while nodeA != nodeB: #Uses a 'while' loop to run through this code as long as 'nodeA' and 'nodeB' are not pointing to the same node. Stops whenever the pointer has either meets or have reached the end of their respective linked list. 
        nodeA = nodeA.next #'nodeA' is moved to the next node in the list 
        nodeB = nodeB.next# 'nodeB' is moved to the next node in the list, and advances both pointers at the same pace 

    return nodeA  # Return the intersection node (or None if there's no intersection)

#Node is building block used to linked list and trees 
#Traversal usually involves iterating through each element, one by one.
