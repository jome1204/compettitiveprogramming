class Solution(object):
    def pancakeSort(self, arr):
        flips = []
        maxx = max(arr)
        sorted_ = sorted(arr)
        
        for i in range (len(arr)):
            
            if arr == sorted_:
                return flips

            k = arr.index(maxx) + 1
            
            if k != 1:
                flips.append(k)
                arr[: k] = reversed(arr[: k])
                
            k = len(arr) - i            
            flips.append(k)
            arr[:k] = reversed(arr[: k])
            maxx -= 1
            
        return flips 
