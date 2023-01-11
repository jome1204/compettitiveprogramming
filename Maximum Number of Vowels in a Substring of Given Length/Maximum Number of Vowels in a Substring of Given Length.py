class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxCount = current = 0
        k -= 1
        
        for i in range(len(s)):
            if i >= k:
                if s[i] in vowels: current += 1
                maxCount= max(maxCount, current)
                if s[i-k] in vowels: current -= 1
            else:
                if s[i] in vowels: current += 1
                    
        return maxCount
