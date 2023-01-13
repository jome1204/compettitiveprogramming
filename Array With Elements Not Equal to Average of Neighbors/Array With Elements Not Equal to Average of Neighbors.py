class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        result = []
        
        p1, p2 = 0, len(nums)-1
        
        while len(result) < len(nums):
            result.append(nums[p1])
            p1 +=1
            
            if p1 <= p2:
                result.append(nums[p2])
                p2 -=1
                
        return result
