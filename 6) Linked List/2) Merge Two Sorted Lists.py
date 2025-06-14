"""
Approach:
Given head of two linked, list merge them and give the head of the sorted one.
Here, we simply make a new linked list aka a new head not pointing to any node.
Then we insert node from among the two linked list whose current node value is smaller.
Then if any of one linked list is fully iterated, we simply stop the loop and add the remaining part of the other linkedin list if left.
"""

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = node = ListNode()
    while list1 and list2:
        if list1.val<=list2.val:
            #we will start adding from the next of the head to avoid seperate unnecessary code to check if its the first check 
            node.next = list1 
            list1 = list1.next    #going on the next element in the list1
        else:
            node.next = list2
            list2 = list2.next
        node = node.next    #after putting the next node at the current node, we proceed to its next node to find next node for it too
    node.next = list1 or list2    #put the remaining linked in the merged linkedin list directly
    return head.next    #the actual head of this merged linked list is the next of head as we started adding from the next of head
            
