class PrefixTree:

    def __init__(self):
        self.root={}
        self.end="*"

    def insert(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.keys():
                curr[char]={}
            curr=curr[char]
        curr[self.end]=True

    def search(self, word: str) -> bool:
        curr=self.root
        for char in word:
            if char not in curr:
                return False
            else:
                curr=curr[char]
        if self.end in curr.keys():
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for char in prefix:
            if char not in curr:
                return False
            else:
                curr=curr[char]
        return True
        