class stack ():
    def __init__ (self): #membuat stack kosong 
        self.item = []
    def empty (self): #mengembalikan nilai bolean yang menunjukan apakah  stack itu kosong
        return len(self) == 0
    def __len__ (self):#mengembalikan banyaknya item di stack
        return len(self.item)
    def peek(self):# mengembalikan nilai posisi atas tanpa menghapus dan mengembalikan nilai dari item yang  paling atas
        assert not self.empty()
        return self.item[-1] 
    def pop(self):#mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stact, menambah item ke puncak stack
        self.item.append(data)
b = stack()
b.push(3)
b.push(9)
b.push(5)
b.push(1)

print (b.pop())
print (b.pop())
print (b.pop())
print("----------------------------------------------------------------------------")
class stack ():
    def __init__ (self): #membuat stack kosong 
        self.item = []
    def empty (self): #mengembalikan nilai bolean yang menunjukan apakah  stack itu kosong
        return len(self) == 0
    def __len__ (self):#mengembalikan banyaknya item di stack
        return len(self.item)
    def peek(self):# mengembalikan nilai posisi atas tanpa menghapus dan mengembalikan nilai dari item yang  paling atas
        assert not self.empty()
        return self.item[-1] 
    def pop(self):#mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stact, menambah item ke puncak stack
        self.item.append(data)
