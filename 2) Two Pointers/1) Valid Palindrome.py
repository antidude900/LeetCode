"""
Approach:
We have to check whether the string given is palindrome or not meaning if its same as its original string even when reversed.
A palindrome only cares about alphanumeric characters! So to make the string more simpler we make a new string with only lowercase alphanumeric characters from the original one
Then we use two pointers, one from the front and one from the back of the string to check whether the characters matches from both the side or not.
"""

def isPalindrome(s: str) -> bool:
    s = ''.join(c.lower() for  c in s if c.isalnum())
    
    #can also do without list comprehension in this way:
    """
    res = ""
    for l in s:
        if l.isalnum():
            res+=l.lower()
    """
  
    i = 0
    j= len(s) - 1
    while (i<j):
        if (s[i] != s[j]):     
            return False     
        i+=1
        j-=1
    return True
