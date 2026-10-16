class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        j = 1
        if len(nums) == 0:
            return []

        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
        return j
