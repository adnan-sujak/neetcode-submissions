class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        del self.stack[-1]
        

    def top(self) -> int:
        last_element = self.stack[-1]
        return last_element
    def getMin(self) -> int:
        smallest_number = min(self.stack)
        return smallest_number
        
