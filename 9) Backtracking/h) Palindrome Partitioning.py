"""
Approach: Given a string s, we have to parition s in such way that every substring of the partition is a palindrome. Then we have to find all such parition solutions.
In this question, we need a helper function to check if every substring we are making is a palindrome or not.
Also, here we will be needing a inner loop which gives us our current index. the reason behind it is that we need our previous index to know where we started from
to make the substring. Here the current index will only can start from the previous index and not before it as the same character cannot be used again to make another substring
You can visualize the previous index as the starting of the new substring and the current index as the potential end. Thus if we go before the previous index, we are using the
character of the previous substring
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
