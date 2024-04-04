'''https://leetcode.com/problems/house-robber-ii/description/

As we can not pick first house and last house together.
We try to pick first house and run till n-1 house keeping track of max.
in Second round, we skip first house and run till nth house keeping track of max.

finally return max of both solutions

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        dp = [0] * len(nums)
        # pick first house and leave last house
        for i in range(len(nums) - 1) :
            dp[i] = max(
                nums[i] + (0 if i-2 < 0 else dp[i-2]),
                (0 if i-1 <0 else dp[i-1])
            )
        ans = max(dp)
        dp = [0] * len(nums)
        dp[0] = 0
        #don't pick first house and pick last house
        for i in range(1, len(nums)) :
            dp[i] = max(
                nums[i] + (0 if i-2 < 0 else dp[i-2]),
                (0 if i-1 < 0 else dp[i-1])
            )
        ans = max(ans, max(dp))
        return ans