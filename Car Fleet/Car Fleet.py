class Solution(object):
    def carFleet(self, target, position, speed):
        carfleet = 0
        lst = []
        stk = []
        for a,b in zip(position,speed):
            lst.append((a,b))
        lst.sort(reverse=True)
        print(lst)
        for p,v in enumerate(lst):
            temp = (target - v[0])/(v[1])
            stk.append(temp)
            size = len(stk)
            if size >= 2 and stk[size-1] <= stk[size-2]:
                stk.pop()
                size -= 1
        answer = size
        
        return answer
        
