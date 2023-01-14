class Solution(object):
    def kthSmallest(self, matrix, k):
        result=[]
        for i in matrix:
            for j in i:
                result.append(j)
        result.sort()
        return result[k-1]
       
