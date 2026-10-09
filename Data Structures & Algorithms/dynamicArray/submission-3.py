class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity =  capacity
        self.size = 0
        self.arr = [0]*capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
 
        if self.size >= self.capacity:
            self.resize()   
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -=1
        i = self.arr[self.size]
        return i
 

    def resize(self) -> None:
        self.capacity *=2 

        arr1 =  [0]*self.capacity
        i = 0
        for n in self.arr:
            arr1[i] = self.arr[i]
            i = i+1
        self.arr = arr1

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        print(self.capacity)
        return self.capacity