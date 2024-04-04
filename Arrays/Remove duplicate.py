'''remove duplicate from sorted array
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

'''
def removeDuplicates(self, nums: List[int]) -> int:
    i,j = 0,0
    while j < len(nums) :
        if nums[i] != nums[j] :
            i += 1
            nums[i] = nums[j]
        j += 1
    return i+1