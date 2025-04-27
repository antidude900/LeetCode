"""
Approach:
We just have to give the top k most frequent elements.
For this: we first count the frequency of each element(using heap for faster access the previous value to increment or use the collector library)
[in my case, i found that collector library decreases efficiency]
Then, we just need to sort according to the frequency(in descending order for highest to come first) and then return the the first k of those
I used various sorting algorithm such as tim sort, heap sort and heap sort with limit of k and here are the results:

Heap sort with limit of k did well than simple heap sort but the tim sort did the best!!!
So i will use tim sort but i will list the other two as well.
"""

def topKFrequent(nums: List[int], k: int) -> List[int]:
    num_map = Counter(nums) 

    """
    Another alternative for num_map = Counter(nums):
    num_map = {}
    for num in nums:
        num_map[num] = num_map.get(num,0)+1
    """
    
    sorted_items = sorted(num_map.items(), key=lambda x: -x[1])
    return [item[0] for item in sorted_items[:k]]

"""
Alternatives using other sorting algorithms:
"""

#Simple Heap Sort:
def topKFrequent(nums: List[int], k: int) -> List[int]:
    num_map = Counter(nums)
    heap = []
      
    for key,value in num_map.items():
        heapq.heappush(heap,(-value,key))

    res = []
    while (len(res)<k):
        res.append(heapq.heappop(heap)[1])
        
    return res

#Heap sort with limit of k:
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    heap = []
    
    for key, val in counter.items():
        heapq.heappush(heap, (val, key))
        if len(heap) > k:
            heapq.heappop(heap)
    
    res = []
    while heap:
        res.append(heapq.heappop(heap)[1])
        
    return res
