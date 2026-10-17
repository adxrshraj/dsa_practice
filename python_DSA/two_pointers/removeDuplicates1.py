class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        j = 0
        k = 1

        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[j+1] = nums[i]
                j += 1
                k += 1
                i += 1
                continue
            i += 1
        return k
            


        
