"""
Approach: Given two linked list in reverse order, add the numbers formed from each and store the answer back in reversed form in another linked list.
If you remember how we added numbers in math classes when we were small, well the answers already there!
We start adding from the last number and then shifting carry to add for the next number.
Here as the linked list is reversed, we automatically starting adding from last.
"""

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    temp = ListNode(None)  #starting the new linked list for the result(will point to the head of the new linked list. 
                           #this makes easy for the iteration of the new linked list putting values at next. 
                           #If we just put value direcly there, now using curr=curr.next for the iteration process wont work as now thought the present node is defined, 
                           #the next node isnt i.e its None)
    curr =  temp  #pointer for the linked list
    carry = 0
    
    while l1 or l2 or carry: #the two numbers maynot be of the same size or the carry comes in the highest place number's addition
        if not (l1 and l2) and not carry: #if one of the two has already finished and there is no carry present, we simply join the remaning as it is
                                          #you might think, if only one linked list remains then doesnt matter if carry exists or not; lets just add the carry to the first of the remaining one and over!
                                          #but what if the carry generates another carry with the number of the remaning one. for eg: [9,9,9,9,9,9] and [1,1,1]
            curr.next = l1 or l2
            break

        #if the linked list still not ended, take the latest value from that list to add. Else it means just the other linked list or carry is left to add.
        val1 = l1.val if l1 else 0  
        val2 = l2.val if l2 else 0
      
        total = val1+val2+carry
        carry = total//10    #the 10th place digit of the sum is the carry
        total = total%10     #the 1th place digit of the sum is the sum for the current digits
        curr.next = ListNode(total)    #storing it in the result linked list

        #storing 
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
      
    return temp.next    #returning the head of the current 
