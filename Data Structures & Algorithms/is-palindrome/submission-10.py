class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            lc, rc = s[l].lower(), s[r].lower()
            if lc.isalnum() and rc.isalnum() and lc != rc:
                return False
                l += 1
                r -= 1
            elif lc.isalnum() and not rc.isalnum():
                r -= 1
            elif not lc.isalnum() and rc.isalnum():
                l += 1
            else:
                l += 1
                r -= 1
        
        return True