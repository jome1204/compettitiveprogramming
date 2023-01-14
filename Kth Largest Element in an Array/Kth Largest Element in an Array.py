class Solution(object):
    def findKthLargest(self, nums, k):
        heap=sorted(nums)
        
        return heap[-k]
#         while(nums and heap[-1]>nums[0]):
#             nums.pop(0)
       
