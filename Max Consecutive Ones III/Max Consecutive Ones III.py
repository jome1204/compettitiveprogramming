class Solution(object):
    def longestOnes(self, nums, k):
        i, j=0, 0

        # float('-inf') is used to set an infinitely large value(such as positive infinity).
        final_result=float('-inf')

        # while loop will run as long as the len(nums) is not less than zero
        while j<len(nums) and i<len(nums):
            if nums[j] != 1:   
                if k>0:
                    k-=1
                else:
                    while k<0 or nums[i]==1:
                        if nums[i]==0:
                            k+=1
                        i+=1
                    i+=1
            final_result=max(final_result,j-i+1)  
            j+=1
        return final_result
