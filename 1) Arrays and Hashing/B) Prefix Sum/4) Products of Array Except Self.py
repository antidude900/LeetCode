"""
Approach:
Here, we have return an array say output where output[i] is the multiplication of all numbers except nums[i]

One of the most simplest apporach will be to find out the total product of nums list and ten assiging each output[i] with total_product/nums[i]

But what if a followup question comes saying not to use division operator to test your dsa knowledge?
For that we simply use both prefix product and postfix product excluding the number itself.
"""

def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1]*len(nums)
    
    prefix = 1
    for i in range(len(nums)):    #prefix product
        res[i] = prefix
        prefix *= nums[i]    #updaing prefix later for not to include the number itself
        
    postfix = 1
    for j in range(len(nums)-1,-1,-1):    #postfix product 
        res[j] *= postfix    #direclty muliplying on the prefix product
        postfix *= nums[j]
    
    return res
