"""
Approach: Given a linked list with each node having next and random pointer, we have to make a deep copy(not referenced copy) of the linked list.
If there was no random pointer, we could have done it in one pass by simply making a new node of each and then connecting them
(by saving the previous copy node by prev and doing prev.next = cpy)
But we have random pointer! This points to any one of the node in the linked list and we dont know which(because its copy may not exists. For next, we can directly create a copy of next to the node 
and there may not be any problem because we can reference that for the next one. for for random, if we make a copy of the random, then referencing it will be hard when we reach to it at the future. 
so we may have made a new copy of the same node for the next of its previous node) So we cant access the copy node to which the random pointer points to directly.
This is why we require two pass! In one pass, we create copy of each node and store them as a value to their original node (so that we can find the copy of any node)
Then in second pass, we find the copy of the nodes pointed by next and random pointer of the original node and then update the next and random pointer of the copy node.

Node: I said that doing in one pass, the referencing will be hard as we will have so much redundant code for each curr, curr.next and curr.random 
(as for each we have to check if its already in the cpyMap dict or not and if its not then we make a new one. So if else for each of the three.
But we can use recursion to simplify the redundant code. so yeah, one pass in viable through recursion
"""

#Two pass
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
    
#One pass
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    cpyMap = {}
    def clone(node):
        #if its the end of the linked list(equivalent to cpyMap = {None:None})
        if not node:    
            return None

        #if we have already made the deep copy of the node(equilavelent to the second pass 1st line)
        if node in cpyMap:    
            return cpyMap[node]

        #if theres no deepcopy, we have its deepcopy(equivalent to 1st pass, first two lines)
        copy = Node(node.val)    
        cpyMap[node] = copy

        #now we again do the same check as above for the next and random pointer and then assign it to the new deepcopy's next and random pointer
        #as per the recursion, the nodes will start being completely built in reverse direction(from end of the linked list to start of the linked list)
        copy.next = clone(node.next)
        copy.random = clone(node.random)
        
        return copy
        
    return clone(head) #the last return of the recursion will be the copy of the head node which is the starting of our deepcopy of the linked list
