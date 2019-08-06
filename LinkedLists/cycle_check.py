# Problem
# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean 
# indicating if the linked list contains a "cycle".

# A cycle is when a node's next point actually points back to a previous node in the list. 
# This is also sometimes known as a circularly linked list.

# Class defintion of singly linked list
class Node (object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None


# SOLUTION
---------
# To solve this problem we will have two markers traversing through the list. marker1 and marker2. 
# We will have both makers begin at the first node of the list and traverse through the linked list. 
# However the second marker, marker2, will move two nodes ahead for every one node that marker1 moves.
# By this logic we can imagine that the markers are "racing" through the linked list, with marker2 moving faster. 
# If the linked list has a cylce and is circularly connected we will have the analogy of a track, 
# in this case the marker2 will eventually be "lapping" the marker1 and they will equal each other.

# If the linked list has no cycle, then marker2 should be able to continue on until the very end, never equaling the first marker

def cycle_check(node):
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        if marker1 == marker2:
            return True
    return False
