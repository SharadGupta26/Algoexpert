'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
https://www.youtube.com/watch?v=U8XENwh8Oy8
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1
        while l <= r :
            m = (l + r) // 2
            if nums[m] == target :
                return m
            if nums[m] >= nums[l] : #left sorted portion
                if target < nums[m] and target >= nums[l] :
                    r = m-1
                else :
                    l = m+1
            else : #right sorted portion
                if target > nums[m] and target <= nums[r] :
                    l = m+1
                else :
                    r = m-1
        return -1