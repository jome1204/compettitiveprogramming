class Solution: 
    def select(self, arr, i):
        size = len(arr)
        min = i
        for k in range(i+1, size):
            if arr[k] < arr[min]:
                min = k

        return min
            
            
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range(0, n):
            min = self.select(arr, i)
            arr[min],arr[i]= arr[i],arr[min]
            
