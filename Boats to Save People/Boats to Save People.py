class Solution(object):
    def numRescueBoats(self, people, limit):
        result = 0
        x = 0
        y = len(people) - 1

        people.sort()

        while x <= y:
            remain = limit - people[y]
            y -= 1
            if people[x] <= remain:
                x += 1
            result += 1

        return result
