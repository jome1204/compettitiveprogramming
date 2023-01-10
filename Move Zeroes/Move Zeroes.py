class Solution(object):
    def moveZeroes(self, nums):
        num = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[i], nums[num] = nums[num], nums[i]
                num += 1
