class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0]*capacity
        self.fullness = 0


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity > self.fullness:  
            self.array[self.fullness] = n
            self.fullness +=1 
        else:
            self.resize()
            self.pushback(n)
    def popback(self) -> int:
        if self.fullness > 0:
            self.fullness -= 1
            return self.array[self.fullness]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0]*self.capacity
        for i in range(len(self.array)):
            new_arr[i] = self.array[i]
        self.array = new_arr


    def getSize(self) -> int:
        return self.fullness
    
    def getCapacity(self) -> int:
        return self.capacity
