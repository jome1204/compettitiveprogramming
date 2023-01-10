class Solution(object):
    def goodDaysToRobBank(self, security, time):
        decreasing = [1]
        counter = 1
        for i in range(1, len(security)):
            if security[i-1] >= security[i]:
                counter += 1
            else:
                counter = 1
            decreasing.append(counter)

        increasing = [1]
        counter = 1
        for i in range(len(security)-2, -1, -1):
            if security[i+1] >= security[i]:
                counter += 1
            else:
                counter = 1
            increasing.append(counter)
        increasing = increasing[::-1]
        ies = []
        for i in range(len(security)):
            if decreasing[i] >= (time+1) and increasing[i] >= (time+1):
                ies.append(i)
        return ies
