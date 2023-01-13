class Solution(object):
    def rank(self, numList, index):
        numList.sort()
        return numList[index]

    def rank2(self, numList, index):
        numList.sort()
        return numList[len(numList) - index]

    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        keys = [i for i in range(1,10001)]
        numberList = {key: [] for key in keys}
        result = ''
        for num in nums:
            numberList[len(num)].append(num)
        
        if len(nums) // 2 > k:
            values = list(numberList.values())
            sumTillNow = 0
            for i in range(len(values)-1, -1, -1):
                sumTillNow += len(values[i])
                if sumTillNow >= k:
                    result =  self.rank2(values[i], k - sumTillNow+len(values[i]))
                    break


        else:
            n = len(nums) - k
            sumTillNow = 0
            
            for value in numberList.values():
                sumTillNow += len(value)
                if sumTillNow > n:
                    result = self.rank(value, n-sumTillNow+len(value))
                    break

        return result
