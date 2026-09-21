class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        times = self.d[key]
        sol = ""
        l, r = 0, len(times) - 1

        while l <= r:
            m = (l + r) // 2

            time = times[m][0]
            if time == timestamp:
                return times[m][1]
            elif time < timestamp:
                sol = times[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return sol