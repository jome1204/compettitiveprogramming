class LargerStrKey(str):
  def __lt__(num, num1) :
    return num + num1 > num1 + num
class Solution(object):
    def largestNumber(self, nums):
         return ''.join(sorted(map(str, nums), key=LargerStrKey)).lstrip('0') or '0'
