class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)

        if length < 2:
            return

        a = [nums[-1]]

        for i in range(length-2,-1,-1):
            if nums[i] < nums[i+1]:
                m = i+1
                for j in range(i+1,length):
                    if nums[j] > nums[i]:
                        if nums[j] < nums[i+1]:
                            m = j

                nums[i], nums[m] = nums[m], nums[i]

                nums[i+1:] = sorted(nums[i+1:])

                return

        for i in range(length//2):
            nums[i],nums[length-1-i] = nums[length-1-i],nums[i]
