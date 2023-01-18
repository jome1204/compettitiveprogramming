class Solution(object):
    def subarraySum(self, nums, k):
        counter = 0
        size = len(nums)
        sum1 = defaultdict(lambda : 0)
        sum2=0
        i = 0
        while i < size:
            sum2 += nums[i]
            if sum2 == k:
                counter +=1
            if sum2-k in sum1:
                temp = sum2-k
                counter += sum1[temp]
            sum1[sum2] += 1  
            i+=1

        return counter
