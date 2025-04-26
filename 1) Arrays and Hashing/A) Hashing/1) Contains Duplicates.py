"""
Approach: Use a hash set to store the seen characters and search them in O(1). 
If the character we are observing rn is already in that set, it means we have duplicate characters.
Else add it to the set and go to the next character.
"""

def hasDuplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

"""
The above solution is equivalent to:
    def hasDuplicate(nums: List[int]) -> bool:
        return (len(set(nums)) != len(nums))
"""
