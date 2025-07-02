"""
Approach: Given a linked list with each node having next and random pointer, we have to make a deep copy(not referenced copy) of the linked list.
If there was no random pointer, we could have done it in one pass by simply making a new node of each and then connecting them
(by saving the previous copy node by prev and doing prev.next = cpy)
But we have random pointer! This points to any one of the node in the linked list and we dont know which. So we cant access the copy node to which the random pointer points to.
This is why we require two pass! In one pass, we create copy of each node and store them as a value to their original node (so that we can find the copy of any node)
Then in second pass, we find the copy of the nodes pointed by next and random pointer of the original node and then update the next and random pointer of the copy node.
"""

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    cpyMap = {None:None} #For the case when we try to find the copy of next and random pointer's node and they point towards null
    
    curr = head
    while curr:    #Making copy of each node
        cpy = Node(curr.val)
        cpyMap[curr] = cpy    #Mapping the original with its copy and storing it
        curr = curr.next
        
    curr = head
    while curr:    #Updating the next and random pointer
        cpy= cpyMap[curr]    #FIrst find the copy of the current node we are in
        cpy.next = cpyMap[curr.next]    #update the copy node's next pointer with the copy of the current node's next pointer
        cpy.random = cpyMap[curr.random]    #update the copy node's random pointer with the copy of the current node's random pointer
        curr = curr.next
        
    return cpyMap[head]                                     
