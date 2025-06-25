"""
Approach: Given a linked list, we have to reorder it such that the twins are together meaning the node n-1-i  comes after node 0 and then connects to the node 1 
which then also follows the same thing. So as we did for the maximum twin sum problem, we have to go the mid and then reverse a half for the iteration of the twins to be easy.
There we did the first half reverse, as we just needed sum and didnt care about the order. But here the linked list should have twins starting from the start and end.
Hence, we reverse the second half and then start iterating from each half and then join each corresponding ones
"""

class Solution:
    def reorderList(head: Optional[ListNode]) -> None:
        fast,slow = head,head
        while (fast and fast.next):    #Going to the mid
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next    #First element of the second half
        prev = slow.next = None    #Disconnecting the first half   

        while second:    #Reversing the second half
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head,prev    #Pointer for the first and second half

        while second:    #Reordering 
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2
