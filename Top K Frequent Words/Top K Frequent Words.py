class Solution(object):
    def topKFrequent(self, words, k):
        result = []
        bucket = [[] for _ in range(len(words) + 1)]

        for word, freq in Counter(words).items():
            bucket[freq].append(word)

        for b in reversed(bucket):
            for word in sorted(b):
                result.append(word)
            if len(result) == k:
                return result
