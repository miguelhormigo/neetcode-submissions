class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = nums2, nums1

        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a) - 1
        while True:
            m = (l + r) // 2
            n = half - m - 2

            aleft = a[m] if m >= 0 else float('-inf')
            aright = a[m + 1] if (m + 1) < len(a) else float('inf')
            bleft = b[n] if n >= 0 else float('-inf')
            bright = b[n + 1] if (n + 1) < len(b) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = m - 1
            else:
                l = m + 1