class TrieNode:
    def __init__(self):
        self.children = {}
        self.refs = 0
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        sol, cur = [], []
        root = TrieNode()

        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.refs += 1
            node.is_end = True

        def dfs(node, r, c):
            if r < 0 or c < 0 or r >= R or c >= C or board[r][c] == '*' or board[r][c] not in node.children:
                return 0
            
            char = board[r][c]
            prev = node
            node = node.children[char]
            board[r][c] = '*'
            cur.append(char)
            
            found = 0
            if node.is_end:
                sol.append(''.join(cur))
                node.is_end = False
                found += 1

            for i, j in [[1,0],[-1,0],[0,1],[0,-1]]:
                found += dfs(node, r + i, c + j)

            node.refs -= found
            if node.refs == 0:
                del prev.children[char]
                
            board[r][c] = char
            cur.pop()

            return found
        
        for r in range(R):
            for c in range(C):
                dfs(root, r, c)
        return sol