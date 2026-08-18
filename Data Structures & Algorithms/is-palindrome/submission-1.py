class Solution:
    def isPalindrome(self, s: str) -> bool:
        si, ei = 0, len(s)-1

        while si < ei:
            if not s[si].isalnum():
                si += 1
            elif not s[ei].isalnum():
                ei -= 1
            else:
                if s[si].lower() != s[ei].lower():
                    return False
                si += 1
                ei -= 1
        return True