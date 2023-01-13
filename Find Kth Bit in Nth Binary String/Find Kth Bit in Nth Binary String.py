class Solution(object):
    def findKthBit(self, n, k):
        return Solution.convert(self,n)[k-1]    

    def convert(self, n):
                if n == 0:
                    return "0"
                first= Solution.convert(self,n-1)
                last = Solution.invert(self,first)

                return first + "1" + last
            
    def invert(self,string):
            replace = ""
            for i in string:
                if i == "0":
                    replace += "1"
                else:
                    replace += "0"
            return Solution.reverse(self,replace)

    def reverse(self,replace):    
            return replace[::-1]
