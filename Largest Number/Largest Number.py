class LargerStrKey(str):
  def __lt__(num1, num2) :
    return num1 + num2 > num2 + num1
class Solution(object):
    def largestNumber(self, nums):
         return ''.join(sorted(map(str, nums), key=LargerStrKey)).lstrip('0') or '0'
