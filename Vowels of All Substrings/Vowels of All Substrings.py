class Solution(object):
    def countVowels(self, word):
        res = [0] * (len(word) + 1)

        for i, c in enumerate(word):
            res[i + 1] = res[i] + (c in 'aeiou') * (i + 1)

        return sum(res)
