class Solution(object):
    def partitionLabels(self, s):
        start = 0
        end = 0
        parts_size = []
        last_occurrence_index = [None] * 26
        n = len(s)
        
        for i in range(n):
            last_occurrence_index[ord(s[i]) - ord('a')] = i
            

        for i in range(n):
            end = max(end, last_occurrence_index[ord(s[i]) - ord('a')])
            
            if i == end:
                parts_size.append(end - start + 1)
                start = end + 1
                
        return parts_size
