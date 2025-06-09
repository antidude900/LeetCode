"""
Approach: Given s1 and s2 strings, we have to check whether any of the s1 permutation is the substring of s2.
s1 permutation is simply s1 but jumbled up. Wait this sounds like one thing we have already done before, Anagram!
Angaram also meant those words which when sorted produce the same word. So yes! Lets apply the algorithm we used in anagram i.e hashmap to solve it
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        #setup the hashmap and window size
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        window_size = len(s1)
        
        # Initialize first window
        for i in range(window_size):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        
        # Slide the window
        for i in range(window_size, len(s2)):
            # Check if window matches
            if s1_count == s2_count:
                return True
                
            # Add new character
            s2_count[s2[i]] += 1
            
            # Remove old character
            old_char = s2[i - window_size]
            s2_count[old_char] -= 1
            if s2_count[old_char] == 0:
                del s2_count[old_char]
            
        return s1_count == s2_count
