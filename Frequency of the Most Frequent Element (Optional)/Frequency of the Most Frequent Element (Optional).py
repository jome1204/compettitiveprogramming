class Solution(object):
    def maxFrequency(self, nums, k):
        size = len(nums)
        nums.sort()
        frequency = 1
        temp = 1
        hold1 = 0
        hold2 = 0
        while size > temp:
            hold1 += (nums[temp] - nums[temp - 1]) * (temp - hold2)
            temp += 1
            while hold1 > k:
                hold1 -= nums[temp - 1] - nums[hold2]
                hold2 += 1
            frequency = max(frequency, temp - hold2)
        return frequency
        
