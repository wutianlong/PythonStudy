class superList(list):
    def __sub__(self,b):
        a= self[:]
        b = b[:]
        
        while len(b) > 0:
            c = b.pop()
            if c in a:
                a.remove(c)
        return a


print superList([1,2,3,4]) - superList([3,4])
