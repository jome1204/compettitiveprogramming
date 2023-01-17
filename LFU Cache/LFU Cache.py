class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.sorted = defaultdict(OrderedDict)
        self.LFU = collections.defaultdict()
        

    def get(self, key):
        if key in self.LFU:
            temp = self.LFU.pop(key)
            tempp = self.sorted[temp].pop(key)
            
        elif key not in self.LFU:
            return -1

       
        if   not self.sorted[self.count] and temp == self.count  :
            self.count+=1
        self.LFU[key]=temp+1
        self.sorted[temp+1][key]=tempp
        return tempp
        

    def put(self, key, value):
        if key in self.LFU and self.capacity>0:
            self.get(key)
            self.sorted[self.LFU[key]][key]=value
            return
        if self.capacity == 0:
            return
        if self.capacity == len(self.LFU):
            i,j = self.sorted[self.count].popitem(last=False)
            self.LFU.pop(i)
        self.count= 1
        self.LFU[key]=1
        self.sorted[1][key]=value

       
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
