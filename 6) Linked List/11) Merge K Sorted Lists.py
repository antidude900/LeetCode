"""
Approach: Given k sorted linked list's heads in the 'lists' list, we have to merge all of the linked lists and return the head of that merged one.
One way that immediately comes in mind, is to merge first two linked list, then merge that linked list with the third and so on.
But in this way, we have to go through all k linked lists each containing say n nodes. so total time complexity is (Nk*k)=(Nk^2):
O(2N) + O(3N) + O(4N) + ... + O(kN) = O(N * (1 + 2 + ... + k)) = O(N * k^2)

But what if we instead of merging linearly,we merge it first dividing into smaller groups and then merging the groups? Yes thats the merge sort algorithm:
for each round, we get a total constant time of O(Nk):

In each round:
- Number of lists halves: k → k/2 → k/4 → k/8 → ...
- Size of each list doubles: N → 2N → 4N → 8N → ...
- Total nodes remain constant ≈ kN
- Total time for each round: O(kN)

and then we have log2(k) rounds so in total time complexity = O(Nk*log2k)
"""

def mergeLists(self,l1,l2): #merging the provided two list
    dhead = ListNode()
    curr = dhead
    while (l1 and l2):
        if l1.val<l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 or l2
    return dhead.next
    
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  #mergining all the k lists provided
    if not lists:
        return None
    
    while (len(lists)>1):  #as we need a pair of two for merging, we do till the length of lists>1. 
                           #If 1, if we can understand the merge has completed and a single linked list is left.
      
        merged = []  #to keep track of the merged linked lists
        for i in range(0,len(lists),2):  #step of 2 as we make a pair of two adjacents(i and i+1)
            l1 = lists[i]
            l2 = lists[i+1] if (i+1)<len(lists) else None
            merged.append(self.mergeLists(l1,l2))  #merge the two adjacent linked lists
        lists = merged  #update the lists with the merged linked lists
    return lists[0]  #return the remaning linked list i.e our final merged one
