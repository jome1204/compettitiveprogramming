class Solution(object):
    def minIncrementForUnique(self, nums):
        if not nums:
            return 0
        nums.sort()

        pre =nums[0]
        n=len(nums )
        ans=0

        for i in range(1, n):
            cur=nums[i]
            if cur<=pre:
                ans+=(pre-cur )+1
                cur=pre+1
            pre=cur
        return ans
        
