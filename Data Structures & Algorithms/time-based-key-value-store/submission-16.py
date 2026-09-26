from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])        

    def get(self, key: str, timestamp: int) -> str:
        res = ["", float('inf')]

        vals = self.store[key]
        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r) // 2

            if vals[m][1] <= timestamp:
                res = vals[m]
                l = m + 1
            else:
                r = m - 1
        
        return res[0]