'''
https://leetcode.com/problems/longest-increasing-subsequence/description/

https://www.youtube.com/watch?v=cjWnW0hdF1Y
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in reversed(range(len(nums))) :
            for j in range(i +1, len(nums)) :
                if nums[i] < nums[j] :
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)