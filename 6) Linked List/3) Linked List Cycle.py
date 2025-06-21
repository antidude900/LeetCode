"""
Approach:
Given a linked list, we have to find whether the linked list contains a cycle or not.
A simple approach is that we can iterate through the linked list storing the node in a hashset. 
if ever during the iteration we find the node in the hashset, we can know its a cycle.

Another way is using fast and slow pointer. the slow pointer moves one step at a time whereas the fast pointer moves 2 steps at a time.
thus, the fast pointer is double in speed of the slow pointer. hence if there is a cycle in the linked list, its certain the fast and slow pointer will overlap
"""

def hasCycle(head: Optional[ListNode]) -> bool:
    f,s = head,head
    while f and f.next:
        f = f.next.next
        s = s.next
        if f == s:
            return True
    return False
