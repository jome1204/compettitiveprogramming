class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        result = 0
        score = 0
        x = deque(sorted(tokens))

        while x and (power >= x[0] or score):
            while x and power >= x[0]:

                power -= x.popleft()
                score += 1
            result = max(result, score)
            if x and score:

                power += x.pop()
                score -= 1

        return result
