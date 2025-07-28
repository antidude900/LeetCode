"""
Approach: Given two arrays s and t; we have to find the minimum length subarray from s which which contains all the characters as in t.

We can create a dictionary for both s and t where we put all the elements of t for the dictionary of t say tCount and for dictionary of s say sCount, 
for each insertion we check if the key in it that are also in the tCount say intersectionKeys have same value or not. 

But for each insertion checking if all the intersectionKeys have same values require O(n*k) where n is size of s and k is size of t (sCount == tCount also require O(k))
But we can avoid the k comparisons by using flags: have and need. For each insertion, we just check if the key is the intersectionKey and if the values are same.
If yes, we increment the have value and if it equals to the need(need = len(tMap) which is the no of intersectionKeys), 
it indicates that all the intersectionKeys have same value and thus the substring rn that forms the sCount contains all the characters as in t. 

And yes for the substring, we use two pointers. When iterating through the s array and inserting to the sCount, 
we use right pointer and for decreasing the size of the window after we met the condition head=tail, 
we decrease the size of the window through left pointer for finding more minimum length subarray
"""

def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
      
    tCount, sCount = {},{}
    for c in t:
        tCount[c] = tCount.get(c,0)+1
    
    have, need = 0, len(tCount)
    l = 0
    res, resLen = [-1,-1], float("inf") #could have direcly stored the syring in res but slicing every single update brings performance issue
    
    for r,c in enumerate(s):
        sCount[c] =  sCount.get(c,0)+1
        if c in tCount and tCount[c] == sCount[c]:
            have+=1
          
        while (have == need):
            if r-l+1 < resLen:
                res = [l,r]
                resLen =r-l+1
              
            c = s[l]
            sCount[c]-=1
            if c in tCount and sCount[c]<tCount[c]:
                have-=1
            l+=1
          
    l, r = res
    return s[l:r+1] if resLen!=float("inf") else ""
    
