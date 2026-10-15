class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_end = True
        
    def search(self, word: str) -> bool:
        return self._backtrack(word, 0, self.root)
    
    def _backtrack(self, word, i, node):
        if i == len(word):
            if node.is_end:
                return True
            return False
        if not node:
            return False

        if word[i] == '.':
            for c in node.children:
                if self._backtrack(word, i+1, node.children[c]):
                    return True
            return False
        else:
            if word[i] not in node.children:
                return False
            else:
                return self._backtrack(word, i+1, node.children[word[i]])
        
        return True