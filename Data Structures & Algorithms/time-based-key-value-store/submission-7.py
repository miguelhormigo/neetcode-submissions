from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.d:
            self.d[key] = [[timestamp, value]]
        else:
            self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ''

        keys = self.d[key]
        l, r = 0, len(keys) - 1
        res = keys[-1]

        while l <= r:
            m = (l + r) // 2
            if keys[m][0] <= timestamp:
                res = keys[m]
                l = m + 1
            else:
                r = m - 1

        if res[0] <= timestamp:
            return res[1]
        return ''