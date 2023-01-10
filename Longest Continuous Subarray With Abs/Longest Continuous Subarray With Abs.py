class Solution(object):
    def longestSubarray(self, nums, limit):
        length=1
        maximum=nums[0]
        minimum=nums[0]
        curr=nums[0:1]
        for i in range(1,len(nums)):
            curr.append(nums[i])
            if nums[i]>maximum:
                maximum=nums[i]
            if nums[i]<minimum:
                minimum=nums[i]

            if maximum-minimum<=limit:
                if len(curr)>length:
                    length=len(curr)
            else:
                curr.pop(0)
                while  max(curr)-min(curr)>limit:
                    curr.pop(0)
                maximum=max(curr)
                minimum=min(curr)
        return length
