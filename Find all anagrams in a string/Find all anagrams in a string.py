class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        pLen = len(p)
        sLen = len(s)
        if pLen > sLen:
            return result
        
        freq = defaultdict(int)
        for i in p:
            freq[i] += 1

        for i in range(pLen):
            if s[i] in p:
                freq[s[i]] -= 1
            
        for i in range(-1, sLen - pLen):
            if i > -1:
                if s[i] in p:
                    freq[s[i]] += 1
                if s[i + pLen] in p:
                    freq[s[i + pLen]] -= 1
                    
            if all(v == 0 for v in freq.values()):
                result.append(i + 1)
                
                
        return result
