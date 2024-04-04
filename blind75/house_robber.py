'''
https://leetcode.com/problems/house-robber/description/

'''

#using DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1 :
            dp [1] = max(nums[1], nums[0])
        for i in range(2, len(nums)) :
            dp[i] = max(dp[i-1] , nums[i] + dp[i-2])
        return max(dp)


#Using DFS and memory
class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        return self.rob_recur(nums, 0, mem)
    def rob_recur(self, nums, i, mem) :
        if i >= len(nums) :
            return 0
        if i in mem :
            return mem[i]
        a = nums[i] + self.rob_recur(nums, i+2, mem)
        b = self.rob_recur(nums, i+1, mem)
        ans = max(a,b)
        mem[i] = ans
        return ans