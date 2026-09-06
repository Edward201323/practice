class MinStack:

    def __init__(self):
        self.arr = []
        self.size = 0


    def push(self, val: int) -> None:
        if self.size == 0:
            self.arr.append((val, val))
            self.size += 1
        else:
            min_val = self.arr[self.size - 1][1]
            if val < min_val:
                min_val = val

            self.arr.append((val, min_val))
            self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return None

        returned_value = self.arr[self.size - 1][0]
        self.arr.pop(self.size - 1)
        self.size -= 1

        return returned_value

    def top(self) -> int:
        if self.size == 0:
            return None
    
        return self.arr[self.size - 1][0]

    def getMin(self) -> int:
        if self.size == 0:
            return None
        return self.arr[self.size - 1][1]