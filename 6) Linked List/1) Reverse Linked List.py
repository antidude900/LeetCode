"""
Approach:
Given a head of a linked list, return the head of the reversed linked list.
Here we simply take a prev node and using it, we make the next of every node in the linked list equal to prev
"""

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev,curr = None,head
  
    while curr:
        temp = curr.next    
        curr.next = prev    #setting next of the current node to the previous node
        prev = curr    #setting previous node to the current node for the upcoming node
        curr = temp    #setting the current node to its next node to get the upcoming node
    return prev
