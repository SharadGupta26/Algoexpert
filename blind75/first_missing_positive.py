'''https://leetcode.com/problems/first-missing-positive/description/'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) :
            val = nums[i]
            if i == val-1 :
                i += 1
            elif val <= 0 or val >= len(nums) :
                i += 1
            elif nums[i] != nums[val-1] :
                nums[i], nums[val-1] = nums[val-1], nums[i]
            else :
                i +=1
        
        for i in range(len(nums)) :
            if i != nums[i] - 1 :
                return i+1
        return nums[-1] + 1

