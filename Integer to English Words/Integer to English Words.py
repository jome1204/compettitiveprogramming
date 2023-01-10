class Solution(object):
    def numberToWords(self, num):
        self.less20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"];
        if num == 0 :
            return "Zero"
        coll = ''
        i = 0
        while num>0:
            if num%1000 != 0:
                coll = self.helper(num%1000) + self.thousands[i] + " " + coll
            num //= 1000
            i += 1
        return coll.strip()

    def helper(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.less20[num] + " "
        if num < 100:
            return self.tens[num//10] + " " + self.helper(num%10)
        if num < 1000:
            return self.less20[num//100] + " Hundred " + self.helper(num%100)
