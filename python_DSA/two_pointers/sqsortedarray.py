class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return []
        n = len(nums)

        sqnums = [0] * n

        i = 0
        j = n - 1
        k = n - 1
        

        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                sqnums[k] = nums[j] ** 2
                j -= 1
                k -= 1
            else:
                sqnums[k] = nums[i] ** 2
                i += 1
                k -= 1
        return sqnums






        
