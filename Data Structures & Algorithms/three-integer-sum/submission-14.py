class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        sols = []

        i = 0
        while i < len(s) - 2:
            l, r = i + 1, len(s) - 1

            while l < r:
                cur_sum = s[i] + s[l] + s[r]

                if cur_sum == 0:
                    sols.append([s[i], s[l], s[r]])

                    l += 1
                    r -= 1

                    while l < r and s[l] == s[l - 1]:
                        l += 1

                    while l < r and s[r] == s[r + 1]:
                        r -= 1

                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1

            i += 1

            while i < len(s) and s[i] == s[i - 1]:
                i += 1

        return sols