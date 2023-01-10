class Solution(object):
    def findTheWinner(self, n, k):
        people = [False] * n

        count = n
        pointer = 0  

        while count > 1:
            for _ in range(k):
                while people[pointer % n]: 
                    pointer += 1  
                pointer += 1
            people[(pointer - 1) % n] = True
            count -= 1

        pointer = 0
        while people[pointer]:
            pointer += 1

        return pointer + 1
