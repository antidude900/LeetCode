"""
Approach:
We have to find the maximum twin sum from the given linked list where twin for the ith indexed node is n-1-ith indexed node.
One very simple way is just to store the values of the nodes in an array and then iterate through the ceil half of the array and find each's twin sum.

But we have to make a new data structure for it. Can we do it without making one?
Yes through, fast and slow pointer. As we know fast pointer moves double the speed of the slow pointer. 
So, the slow pointer reaches the ceil half of the list when the fast pointer reaches the end.
Another thing to understand is that the twins are just the corresponding same positions form first and last i.e 1 and n, 2 and n-1 and so on.
So, what we do is start from the middle and thus one pointer goes to the left from the middle and one to the right each time pointer containing the twins.
But to go the left from the middle, we cant simply do in simple linked list.so we have to reverse the left half to perform that operation.
As we can see this method depends on the symmetry of the node. Hence it doesnt work for the odd size.
"""

def pairSum(self, head: Optional[ListNode]) -> int:
    fast, slow = head,head
    prev = None
    while fast and fast.next: #reveresing until we reach middle
        fast = fast.next.next
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    #reached middle and now iterating left and right from the middle getting the twins
    res = 0
    while (slow):
        res = max(res,prev.val+slow.val)
        prev = prev.next
        slow = slow.next
    return res

#Using a array/list
class Solution:
    def pairSum(head: Optional[ListNode]) -> int:
        res = float("-inf")
        indexed = []
        temp = head

        while temp:
            indexed.append(temp.val)
            temp = temp.next

        n = len(indexed)
        for i in range(n//2+1):
            res = max(res,indexed[n-1-i]+indexed[i])
        return res

