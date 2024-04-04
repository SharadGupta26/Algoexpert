'''https://leetcode.com/problems/product-of-array-except-self/
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)
        res = [0]*len(nums)
        for i in range(len(nums)) :
            prefix[i+1] = prefix[i] * nums[i]
        
        for i in reversed(range(len(nums))) :
            postfix[i] = postfix[i+1] * nums[i]

        
        for i in range(len(nums)) :
            res[i] = prefix[i] * postfix[i+1]
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pre = 1
        for i in range(len(nums)) :
            ans[i] = pre
            pre *= nums[i]

        post = 1
        for i in reversed(range(len(nums))) :
            ans[i] *= post
            post *= nums[i]
        return ans