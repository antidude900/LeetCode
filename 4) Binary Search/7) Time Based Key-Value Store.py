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
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.timestamps[key]

        #timestamp can get less than the previous one irl. so the next one wont be smaller than the previous one. so the smallest timestamp is the first one and the biggest one is the last one
        #so if the given timestamp is less than the first one, there's no solution.
        if not vals or timestamp<vals[0][0]:
            return ""

        #and if the given timestamp is greater than the last one, the nearest smaller one is the last one
        if timestamp > vals[-1][0]: 
            return vals[-1][1]

        l, r = 0, len(vals)-1
        res = ""
        
        while l <= r:
            m = l+(r - l) // 2
            if timestamp == vals[m][0]:
                return vals[m][1]
                
            elif timestamp > vals[m][0]:
                l = m+1
                res = vals[m][1] #as this timestamp is less than the timestamp we require, it might be the timestamp_prev result value
            else:
                r = m-1
                
        return res    #at the end, the latest value which is less than the timestamp will be final timestamp_prev for the output(if we dont find the exact timestamp)
