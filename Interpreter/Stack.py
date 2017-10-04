class Stack:
    def __init__(self):
        self.s = []
    
    def rotate(self, n):
        if self.height() != 0:
            n = n % self.height()
            self.s = self.s[n:] + self.s[:n]
    
    def push(self, item):
        self.s.append(item)
    
    def pop(self):
        self.__height_check()
        return self.s.pop()
    
    def peek(self):
        self.__height_check()
        return self.s[-1]
    
    def height(self):
        return len(self.s)
    
    def contents(self):
        out = ""
        for i in self.s:
            out += str(i) + "\n"
        return out
    
    def __height_check(self):
        if self.height() == 0:
            raise IndexError("Stack is empty.")