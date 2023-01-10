class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greatest = {}
        for i in range(len(nums2)): 
            while len(stack) > 0 and stack[-1][0] < nums2[i]: 
                val, index = stack.pop()
                next_greatest[val] = nums2[i]      
            stack.append((nums2[i], i))


        answer = []
        for i in range(len(nums1)): 
            if nums1[i] in next_greatest: 
                answer.append(next_greatest[nums1[i]])
            else: 
                answer.append(-1)

        return answer
