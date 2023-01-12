class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strlen, substr = 0, []
        for i in s:
            if i not in substr:
                substr.append(i)
            else:
                strlen  = max(strlen, len(substr))
                substr = substr[substr.index(i) + 1:]
                substr.append(i)
        return max(strlen, len(substr))
