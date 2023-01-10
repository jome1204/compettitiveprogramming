class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        num = 2
        a = 1
        b = 0

        while n>=num:
            ans = a + b
            b=a
            a=ans
            num+=1
        return ans
