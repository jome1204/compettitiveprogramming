class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        return (math.log10(n) / math.log10(4))%1 == 0
