"""
Apporach:
To find anagrams, we have to check whether they contains exact same characters but the order may vary.
The first thing that might come in mind is sorting and then checking if two strings are same or not but this takes O(nlogn) time complexity 

The better way is using hash maps in which we store the frequency of each character and then check if hash maps for both strings are same or not
"""

def isAnagram(s: str, t: str) -> bool:
    if (len(s)!=len(t)):
        return False
    s_map={}
    t_map={}
    for i in range(len(s)):
        s_map[s[i]] = s_map.get(s[i],0) + 1    #we are simply incrementing the previous frequency by 1
        t_map[t[i]] = t_map.get(t[i],0) + 1    
    
    return s_map == t_map
