class Solution(object):
    def compress(self, chars):
        slow, fast, end = 0, 0, 0
        while fast < len(chars):
            while fast < len(chars) and chars[slow] == chars[fast]:
                fast += 1
            chars[end] = chars[slow]
            end += 1
            
            if fast - slow > 1:
                for i in str(fast - slow):
                    chars[end] = i
                    end += 1
            
            slow = fast
            
        for i in range(len(chars) - end):
            chars.pop()

        return end
