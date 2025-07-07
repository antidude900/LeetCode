"""
Approach: We are given a linked list, and we have to reverese the nodes in group of k meaning first we seperate the linked list into multiple groups, 
reverse them and then link them together. You might feel its a simple reverse linked list question with just some 'group' requirement 
but tbh there are many extra cases that come with this 'group' requirement. The next of the first node of a group should be pointing towards the kth element of another group.
This adds a whole new layer to the question and thus we have to keep track of groupPrev(previous node before the group) and groupNext(previous node after the group)
"""

def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dhead = ListNode(next=head)    #To make iteration more easier, we use a dummy head
    groupPrev = dhead    #stores the previous node before the current group. This will help us connect the groups
  
    while True:    #making as much as groups possible
        kth = self.getKth(groupPrev,k)    #get the kth node
        
        if not kth:    #if None is encountered before making a group, we cannot make further groups
            break
            
        prev = groupNext = kth.next    #the next node after the group is kth.next and this will be used as the stop condition for the reversing in the group
                                       #and also it is the next of the first element in the previous proup before reversing
        curr = groupPrev.next    #the first node of the group
        
        while curr != groupNext:    #simple reversing of linked list
            temp =  curr.next    
            curr.next = prev    #at first, the next of the first node will be set to next node after the group as the first node becomes the last node of the group after reversing
                                #then, simple backlinking(next pointing to the previous) happens
            prev = curr    
            curr = temp
            
        temp = groupPrev.next    #after reversing, we have to change the first node of the group i.e groupPrev.next to the kth node
                                 #and also change groupPrev to the last node(which was the first node i.e groupPrev.next before reveresing)
                                 #so as we need to change the value of groupPrev.next as per the first criteria, we store its initial value for the second criteria
        groupPrev.next = kth    #first criteria
        groupPrev = temp    #second criteria
        
    return dhead.next

def getKth(self,node,k):   #get the kth node
    while (node and k>0):    #if the loop ends by the first condition we return None and if ends by the second condition we return kth node
        node = node.next
        k -= 1
    return node
