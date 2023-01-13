class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        operation = 0
        to_right = 0
        to_left = len(nums)-1
      
        while to_right < to_left:
            if nums[to_right] +nums[to_left]<k:

                to_right+=1
            elif nums[to_right] +nums[to_left]==k:
                operation +=1
                to_right+=1
                to_left-=1
         
          
            else:
                to_left-=1
        return operation
