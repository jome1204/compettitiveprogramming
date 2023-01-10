class Solution(object):
    def isValid(self, s):
        brack_checker = [('{', '}'), ('(', ')'), ('[', ']')]
        stack = []
        for i in s:
            if len(stack)>0 and (stack[-1], i) in brack_checker:
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0
