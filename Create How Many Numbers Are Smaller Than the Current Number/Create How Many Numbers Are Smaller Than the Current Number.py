class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l=len(nums)
        result=[]
        count=0
        for i in nums:
            for j in range(l):
               if (nums[j]-i)<0:
                   count+=1
            result.append(count)
            count=0
        return result
