class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            
            if diff > 0:
                heapq.heappush(heap, -diff)
                bricks -= diff
            if bricks < 0:
                if ladders > 0:
                    ladders -= 1
                    bricks += -heapq.heappop(heap)
                else:
                    return i-1
        return len(heights)-1
