# Stack implementation

class Stack:
    def __init__(self, size: int):
        self.buf = [0] * size
        self.sp = -1

    def push(self, number: int) -> None:
        self.sp += 1
        self.buf[self.sp] = number
    
    def pop(self) -> int:
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def top(self) -> int:
        return self.buf[self.sp]
    
    def is_empty(self):
        return len(self.buf) == 0
