class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        
        return i
