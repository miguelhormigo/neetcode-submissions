class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = nums2, nums1
        
        total = (len(a) + len(b))
        half = total // 2

        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            aleft = a[i] if i >= 0 else float('-inf')
            aright = a[i + 1] if i < len(a) - 1 else float('inf')
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j + 1] if j < len(b) - 1 else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                return (min(aright, bright) + max(aleft, bleft)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1