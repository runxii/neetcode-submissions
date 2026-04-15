class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        # key stacks
        self.k=[]
        self.size=0
        self.capacity=capacity

    def get(self, key: int) -> int:
        print(f'Before get keys: {self.k}, cache:{self.cache}')
        if key in self.k:
            # renew least visited key
            self.k.remove(key)
            self.k.append(key)
            print(f'After get keys: {self.k}, cache:{self.cache}')
            return self.cache[key]
        return -1
    def put(self, key: int, value: int) -> None:
        self.cache[key]=value
        if key not in self.k:
            self.size+=1
        else:
            self.k.remove(key)
        self.k.append(key)
        print(f'After put keys: {self.k}, size: {self.size}, cache:{self.cache}')

        if self.size>self.capacity:
            # delete least used key, FIFO (head)
            del self.cache[self.k[0]]
            del self.k[0]

            print(f'current keys: {self.k}, size: {self.size}, cache:{self.cache}')
            # size-1
            self.size-=1
