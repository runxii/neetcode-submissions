class WordDictionary:

    def __init__(self):
        self.root={}
        self.end="*"

    def addWord(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.keys():
                curr[char]={}
            curr=curr[char]
        curr[self.end]=True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr:
                        if child != self.end and dfs(i + 1, curr[child]):
                            return True
                    return False
                else:
                    if char not in curr:
                        return False
                    curr = curr[char]
            return self.end in curr

        return dfs(0, self.root)