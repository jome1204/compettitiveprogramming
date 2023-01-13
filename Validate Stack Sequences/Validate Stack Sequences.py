class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        index = 0 

        for p in pushed: 
            stack.append(p)
            while stack and index<len(popped) and stack[-1]==popped[index]:
                index += 1 
                stack.pop()
                
        return stack ==[]
      
