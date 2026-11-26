class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                print(cur.is_end)
                return cur.is_end
            
            l = word[i]

            if l == '.':
                for c in cur.children:
                    if dfs(i + 1, cur.children[c]):
                        return True
            elif l in cur.children:
                return dfs(i + 1, cur.children[l])
            return False
        
        return dfs(0, self.root)