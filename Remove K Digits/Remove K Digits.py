class Solution(object):
    def removeKdigits(self, num, k):
        tempStack = []
        for i in num:
            while (len(tempStack) != 0) and k > 0 and tempStack[-1] > i:
                tempStack.pop()
                k -=1
            tempStack.append(i)
            
        tempStack = tempStack[:len(tempStack)-k]
        output = ''.join(tempStack)
        if len(output) > 0:
            return str(int(output))
        else:
            return '0'
