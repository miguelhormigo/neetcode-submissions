class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        result = []

        for i, n in enumerate(sn):
            if i > 0 and n == sn[i-1]:
                continue

            l, r = i + 1, len(sn) - 1

            while l < r:
                csum =  sn[i] + sn[l] + sn[r]
                if csum > 0:
                    r -= 1
                    while l < r and sn[r] == sn[r + 1]:
                        r -= 1
                elif csum < 0:
                    l += 1
                    while l < r and sn[l] == sn[l - 1]:
                        l += 1
                else:
                    result.append([sn[i], sn[l], sn[r]])
                    l += 1
                    while l < r and sn[l] == sn[l - 1]:
                        l += 1
        
        return result