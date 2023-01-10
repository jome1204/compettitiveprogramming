class Solution(object):
    def fizzBuzz(self, n):
        a = "FizzBuzz"
        b = "Fizz"
        c = "Buzz"
        arr=[]
        for i in range(1,n+1):
            arrset=""
            if i%3==0 and i%5==0:
                arrset += a
            elif i%3==0:
                arrset+=b
            elif i%5==0:
                arrset+=c
            else:
                arrset += str(i)
            arr.append(arrset)
        return arr
