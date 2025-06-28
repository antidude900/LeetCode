"""
Approach: Given the head of a linked list, we have to remove the 'n'th node from the end.
For this we have to set up the left and right pointer starting from the head and then distance the left and right by n.
Now when traversing both the left and right pointer, when the right pointer reaches the end; the left pointer reaches the node to be removed.
But we have to get the node ahead of the node to be the deleted for the removal.
So we make a dummy head and start the left from there where the right starts from the real head. 
In this way, we will get the distance of n+1 and thus node ahead of the node to be removed.
"""
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dhead = ListNode(next=head)
    left = dhead
    right = head
    while n>0: #setting up the n+1 distance
               #we simply didnt do the n+1>0 instead of the dummy head because just think of removing in the head. it will result to right=none.next
               #so we dont want to take risk of incrementing more than the given counter which may lead to overflow
        right = right.next
        n-=1
        
    while right: #finding the prev node before the node to be removed
        left, right = left.next, right.next
    
    left.next = left.next.next #replacing the prev node's next to the node to be removed's next
    return dhead.next    #the dummy head's next is the real head (thus this dummy head also solved the problem of removing the head)
