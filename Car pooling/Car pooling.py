class Solution(object):
    def carPooling(self, trips, capacity):
        total = 0
        store = []
        for passenger, from_, to in trips:
            store.append((from_, passenger))
            store.append((to, -passenger))
        store.sort()
        for num in store:
            total += num[1]
            if total > capacity:
                return False
        return True
