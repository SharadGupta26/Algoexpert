'''
https://leetcode.com/problems/maximum-product-subarray/

https://www.youtube.com/watch?v=lXVy6YWFcRM
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        cmin, cmax = 1,1
        for n in nums :
            if n == 0 :
                cmin, cmax = 1,1
                continue
            tmp = cmax * n
            cmax = max(cmax * n, cmin * n, n)
            cmin = min(tmp, cmin * n, n)
            ans = max(ans, cmax)
        return ans