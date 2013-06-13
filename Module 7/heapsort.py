# Heapsort
class Heap: 
    def __init__(self, lst):
        self.list = [len(lst)] + lst
        k = self.poslastparent()
        while k >= self.posroot():
            self.sink(k)
            k -= 1
        
    def insert(self, val):
        self.list[0]+=1
        self.list.append(val)
        self.swim(len(self.list)-1)
        
    def swim(self, node_idx):
        while node_idx > self.posroot() and \
                self.list[node_idx] > self.list[self.parent(node_idx)]:
            self.exch(node_idx, self.parent(node_idx))
            node_idx//=2
            
    def delmax(self):
        max = self.list[self.posroot()]
        self.exch(self.poslast(), self.posroot())
        del self.list[-1]
        self.list[0] -=1
        self.sink(self.posroot())
        return max
        
    def sink(self, node_idx):
        while node_idx <= self.poslastparent():
            j = self.leftchild(node_idx)
            if self.rightchild(node_idx) <= self.poslast():
                if self.list[self.rightchild(node_idx)] > \
                        self.list[self.leftchild(node_idx)]:
                    j = self.rightchild(node_idx)
            if self.list[j] > self.list[node_idx]:
                self.exch(j, node_idx)
            else:
                break
            node_idx = j
    
    def exch(self, a,b):
        self.list[a], self.list[b] = self.list[b], self.list[a]
        
    def parent(self,n): return n//2
        
    def leftchild(self, n): return n*2
        
    def rightchild(self,n): return n*2+1
        
    def poslast(self): return self.list[0]
        
    def posroot(self): return 1
        
    def poslastparent(self): return self.parent(self.poslast())
    
        
def sort(lst):
    heap = Heap(lst)
    while heap.poslast() > 1:
        heap.exch(heap.poslast(), heap.posroot())
        heap.list[0]-=1
        heap.sink(heap.posroot())
    return heap.list[1:]
        
