from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        keys = list(self.d[key].keys())
        if not keys:
            return ''
            
        l, r = 0, len(keys) - 1
        res = float('inf')

        while l <= r:
            m = (l + r) // 2
            if keys[m] <= timestamp:
                res = keys[m]
                l = m + 1
            else:
                r = m - 1

        if res <= keys[-1]:
            return self.d[key][res]
        return ''