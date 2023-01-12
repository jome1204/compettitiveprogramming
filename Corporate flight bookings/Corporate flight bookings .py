class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        prefixsum = [0]*(n-k+1)
        result  = [0]*3
        maxsum = 0
      
        
        for i in range(k):
            prefixsum[0] += nums[i]
 
        for i in range(1,n+1-k):
            prefixsum[i] = prefixsum[i-1] + nums[i+k-1] - nums[i-1]
         
        h = len(prefixsum)
        leftidx = [0]*h
        rightidx = [0]*h
        
        idx = 0
        for i in range(h):
            if prefixsum[i]>prefixsum[idx]:
                idx = i
            leftidx[i] = idx
       
        idx = h-1
        for i in range(h-1,-1,-1):
            if prefixsum[i]>=prefixsum[idx]:
                idx = i
            rightidx[i] = idx
         
        for mid in range(k,h-k):
            left, right = leftidx[mid-k],rightidx[mid+k]
            total = prefixsum[left] + prefixsum[mid] + prefixsum[right]
            if total > maxsum:
                result[0] = left
                result[1] = mid 
                result[2] = right 
            maxsum = max(maxsum,total) 
        
        return result
