class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = {i: [] for i in keyName}
        records = sorted(zip(keyName, keyTime))
        
        for name, time in records:
            times[name].append(time)
            
        minutes = lambda x: int(x[:2]) * 60 + int(x[3:])
        
        alerted = []
        for name in sorted(times.keys()):
            for i in range(2, len(times[name])):
                if minutes(times[name][i]) - minutes(times[name][i - 2]) <= 60:
                    alerted.append(name)
                    break
        return alerted