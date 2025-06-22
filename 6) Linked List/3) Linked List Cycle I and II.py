"""
Approach:
Given a linked list, we have to find whether the linked list contains a cycle or not. And if yes, return the head of the cycle
A simple approach is that we can iterate through the linked list storing the node in a hashset. 
if ever during the iteration we find the node in the hashset, we can know its a cycle and that node is the head

Another way is using fast and slow pointer. the slow pointer moves one step at a time whereas the fast pointer moves 2 steps at a time.
As a result the distanced between the pointers decrease by one in the cycle and is bound to overlap
This shows that there is cycle in the linked list. 
Now if there is cycle, we find its head. if we start from the head of the linked list and the overlapped position in the cycle and start moving, 
we will meet at the head of the linked list. heres why: 
If the steps from head of list to head of cycle is P, the length of cycle is C and the slow pointer moved C-X in the cycle meaning X part of C was untraveled by slow pointer;
then the total steps walked by the slow pointer upto the overlap is P+(C-X) and fast pointer is P+C+(C-X).
We have the relation:
2*slow_steps = fast_steps (meaning fast pointer covers double the total steps of slow pointer)
2*(P+C-X) = P+C+C-X
2P-P+2C-2C = 2X-X
P = X

Hence, the steps it requires to cover the X remaning part of the cyle and return to the head is equal to the steps it requires to reach the head of the cycle from the head of the list.
Thus we start from both those places and find the head of the cycle where they meet.
"""

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    f,s = head,head
    while f and f.next:
        f = f.next.next
        s = s.next
        if f == s:
            t = head
            while (t!=s):
                t = t.next
                s = s.next
            return t
    return None
