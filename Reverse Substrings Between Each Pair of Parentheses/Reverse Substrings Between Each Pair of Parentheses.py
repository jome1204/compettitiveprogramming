class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c == ')':
                p = stack.pop()
                s = s[:p] + s[i-1:p:-1] + s[i+1:]
                i -= 2
            i += 1
        return s
