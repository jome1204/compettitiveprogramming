class Solution(object):
    def calculate(self, s):
        n = len(s)
        answer = 0
        stk = []
        sign = "+"
        number = 0
        for i in range(n):
            if s[i].isnumeric():
                number = number*10+ int(s[i])
            if s[i] in "+-*/" or i == n-1:
                if sign == "+":
                    stk.append(number)
                elif sign == "-":
                    stk.append(-number)
                elif sign == "*":
                    temp = stk.pop()*number
                    stk.append(temp)
                elif sign == "/":
                    temp = stk.pop()/number
                    stk.append(int(temp))
                number = 0
                sign = s[i]
                
        for results in stk:
            answer += results
        
        return answer
