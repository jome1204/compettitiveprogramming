class Solution(object):
    def decode_util(self, s, begin):
        i = begin
        tempo = 0
        curr_str = ''

        while i < len(s):
            if s[i].isdigit():
                tempo *= 10
                tempo += int(s[i])
                i += 1
            elif s[i] in lowercase:
                curr_str += s[i]
                i += 1
            elif s[i] == '[':
                bracket_decode, last_idx = self.decode_util(s, i+1)
                curr_str += (tempo * bracket_decode)
                i = last_idx + 1
                tempo = 0
            elif s[i] == ']':
                break

        return curr_str, i
    def decodeString(self, s):
        return self.decode_util(s, 0)[0]
