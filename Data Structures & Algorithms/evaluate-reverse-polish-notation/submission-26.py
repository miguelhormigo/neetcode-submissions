class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            if t == '+':
                nums.append(nums.pop() + nums.pop())
            elif t == '*':
                nums.append(nums.pop() * nums.pop())
            elif t == '-':
                b, a = nums.pop(), nums.pop()
                nums.append(a - b)
            elif t == '/':
                b, a = nums.pop(), nums.pop()
                nums.append(int(a / b))
            else:
                nums.append(int(t))
        
        return int(nums[-1])