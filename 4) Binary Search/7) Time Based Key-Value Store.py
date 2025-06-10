"""
Approach:
We have to implement two functions. 
set(key,val,timestamp) will set the value for the key at a timestamp as val.
get(key,timestamp) will give the value of the key at the given timestamp and if that doesn't exist, 
it will give the value at that timestamp nearest smaller to the given timestamp.

As there's not clever trick in this question and it is straight forward, nothing is there to explain more.
"""

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.map[key]
        if not timestamps:
            return ""

        #timestamps can get less than the previous one irl. so the next one wont be smaller than the previous one. so the smallest timestamp is the first one and the biggest one is the last one
        #so if the given timestamp is less than the first one, there's no solution.
        if timestamp < timestamps[0][0]: 
            return ""

        #and if the given timestamp is greater than the last one, the nearest smaller one is the last one
        if timestamp > timestamps[-1][0]: 
            return timestamps[-1][1]

        left, right = 0, len(timestamps)-1
        
        while left <= right:
            mid = left+(right - left) // 2
            if timestamp == timestamps[mid][0]:
                return timestamps[mid][1]
            elif timestamp > timestamps[mid][0]:
                left = mid + 1
            else:
                right = mid -1
        return timestamps[right][1]
