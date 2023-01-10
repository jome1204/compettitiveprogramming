class Solution(object):
    def totalFruit(self, fruits):
        result = 0
        count = defaultdict(int)

        x = 0
        for r, t in enumerate(fruits):
            count[t] += 1
        while len(count) > 2:
            count[fruits[x]] -= 1
            if count[fruits[x]] == 0:
                del count[fruits[x]]
            x += 1
        result = max(result, r - x + 1)

        return result
