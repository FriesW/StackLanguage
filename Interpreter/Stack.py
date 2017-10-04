class Stack:
    def __init__(self):
        self.s = []
    
    def rotate(self, n):
        self.s = self.s[n:] + self.s[:n]
    
    def push(self, item):
        self.s.append(item)
    
    def pop(self):
        return self.s.pop()
    
    def peek(self):
        return self.s[-1]
    
    def height(self):
        return len(self.s)
    
    def contents(self):
        out = ""
        for i in self.s:
            out += str(i) + "\n"
        return out