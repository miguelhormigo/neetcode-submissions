class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        left = 0
        while left < len(height) and height[left] == 0:
            left += 1
        if left == len(height):
            return 0
        hl = height[left]
        
        right = left + 1
        filled = 0
        while right < len(height):
            hr = height[right]
            if hr < hl:
                filled += hr
            else:
                result += min(hl, hr) * (right - left - 1) - filled
                left, hl, filled = right, hr, 0
            right += 1

        print('first:', result)

        # reversed
        right -= 1
        while right > left and height[right] == 0:
            right -= 1
        hr = height[right]

        end, left = left, right - 1
        filled = 0
        print(f'l {left}, r {right}, hl {hl}, hr {hr}, end {end}')
        while left >= end:
            hl = height[left]
            print(left, hl)
            if hl < hr:
                filled += hl
            else:
                print('*', min(hl, hr) * (right - left - 1) - filled)
                result += min(hl, hr) * (right - left - 1) - filled
                right, hr, filled = left, hl, 0
            left -= 1
        
        return result