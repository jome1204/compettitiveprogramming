class Solution(object):
    def minSubArrayLen(self, target, nums):
        if len(nums)==0:
            return 0
        elif len(nums) == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0
        start = 0
        end = 0
        minLength = float("inf")
        sumx = nums[0]
        while(end < len(nums)):
            if sumx < target:
                end+=1
                if (end < len(nums)):
                    sumx+=nums[end]
                else:
                    break
            else:
                minLength = min(minLength, end-start+1)
                sumx -= nums[start]
                start += 1
        if minLength == float("inf"):
            return 0
        return minLength
