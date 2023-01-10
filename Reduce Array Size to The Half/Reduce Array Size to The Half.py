class Solution(object):
    def minSetSize(self, arr):
        length = len(arr)

        count = collections.Counter(arr).most_common()
        count.sort(key=lambda c: -c[1])

        sum = 0
        for i, c in enumerate(count):
            sum += c[1]
            if sum >= length // 2:
                return i + 1
