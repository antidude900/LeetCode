"""
Approach: Given a string s, we have to parition s in such way that every substring of the partition is a palindrome. Then we have to find all such parition solutions.
In this question, we need a helper function to check if every substring we are making is a palindrome or not.
Also, here we will be needing a inner loop which gives us our current index. the reason behind it is that we need our previous index to know where we started from
to make the substring. 
Here the current index only can start from the previous index and not before it as the same character cannot be used again to make another substring in the same partition.
You can visualize the previous index as the starting of the new substring and the current index as the potential end. Thus if we go before the previous index, we are using the
character of the previous substring. 
Also  in the partition we try to make another substring which starts from the character in the next index only if the previous substring was palindrome. If it wasnt palindrome,
the rule that each subtring in the parition should be palidrome is already invalid. So we just keep only the character in the present index as a substring(as a single character
is always palindrome) and then go to the next index to try to make other substrings which are palindrome.
So there will for sure exist atleast one solution(in that solution all substrings are a single character)
"""

def partition(self, s: str) -> List[List[str]]:
    parts, part = [],[]
  
    def backtrack(i):
        if i == len(s):
            parts.append(part.copy())
            return 
          
        for j in range(i,len(s)):
            if self.isPalindrome(s,i,j):
                part.append(s[i:j+1])    
                #This recursion starts always with atleast i in the partition(due to the line above it) 
                #If we start from the first recursion i=0 and in the second i=2. So it also makes sure that all characters are included in tha partition
                #as if we exclude a character, it will be slicing rather than partition
                backtrack(j+1)    
                part.pop()
    backtrack(0)
    return parts
  
def isPalindrome(self,s,l,r):
    while l<r:
        if s[l] != s[r]:
            return False
        l,r = l+1,r-1
    return True
