import operator
class Solution(object):
    def evalRPN(self, tokens):
        if tokens == []:
            return -1

        stack = [] 

        operations = ["+", "-", "*", "/"]
        operations_lookup = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        for token in tokens:            
            if token not in operations:
                stack.append(int(token))
            else:
                res1 = stack.pop(-1)
                res2 = stack.pop(-1)
                result = operations_lookup[token](res2, res1)
                stack.append(int(result))

        return stack.pop()
