class node:
    def __init__(self, val: int):
        self.val = val
        self.node_next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        walker = self.head
        i = 0
        while walker != None and i<index:
            walker = walker.node_next
            i+=1
        if i == index and walker != None:
            return walker.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        n = node(val)
        if self.head == None:
            self.head = n
        else:
            n.node_next = self.head
            self.head= n

    def insertTail(self, val: int) -> None:
        n = node(val)
        if self.head == None:
            self.head = n
        else:
            walker = self.head
            while walker.node_next != None:
                walker = walker.node_next
            walker.node_next = n


    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        if index == 0:
            self.head = self.head.node_next
            return True
        else:
            walker = self.head
            i = 0
            while walker!=None:
                if i == (index -1) and walker.node_next != None:
                    walker.node_next = walker.node_next.node_next
                    return True
                walker = walker.node_next
                i+=1
            if walker == None:
                return False
        

    def getValues(self) -> List[int]:
        l = []
        walker = self.head
        while walker!= None:
            l.append(walker.val)
            walker = walker.node_next
        return l


        
