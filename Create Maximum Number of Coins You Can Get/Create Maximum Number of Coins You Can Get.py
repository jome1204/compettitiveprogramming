class Solution(object):
    def maxCoins(self, piles):
        length = len(piles)
        sorted_piles = sorted(piles)[::-1]
        return sum(sorted_piles[i] for i in range(1, length//3*2+1,2))
