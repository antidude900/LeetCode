"""
Approach:
The algorithm you used for Two Sum I(Unsorted) can even be used here as well!
But as this problem offers a sorted array, we can do without implementing hash set!
This avoids overhead of memory allocation and hashing.

In this new apporach, we use two pointers and update the pointers postition as we do in binary search.
Here we do the sum of the numbers of the two pointers. If the sum comes equal to target, then we have the answer.
But if the sum comes greater than target, then we have to update in such a way that it decreases the sum!
This is possible by decreasing the rightmost pointer which is pointing at the biggest number(as ascending order)
Similarly if sum comes less than target, then we have to update in such a way that it increases the sum!
which is by increasing the leftmost pointer.
We update in this manner until we get the required result or until the left pointer passes the right pointer.
"""

def twoSum(numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers)-1
    while(i<j):
        if (numbers[i]+numbers[j] == target):
            return [i+1,j+1]
        elif (numbers[i]+numbers[j]>target):
            j-=1
        else:
            i+=1
        
