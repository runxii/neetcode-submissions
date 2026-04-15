class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr=nums
        self.rank=k

    def add(self, val: int) -> int:
        self.arr.append(val)
        currentArray=sorted(self.arr)
        currentArray.reverse()
        return currentArray[self.rank-1]
