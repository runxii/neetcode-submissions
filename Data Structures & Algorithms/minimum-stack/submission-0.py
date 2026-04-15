class MinStack:

    def __init__(self):
        self.arr=[]

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        p=len(self.arr)
        return self.arr[p-1]

    def getMin(self) -> int:
        return min(self.arr)
