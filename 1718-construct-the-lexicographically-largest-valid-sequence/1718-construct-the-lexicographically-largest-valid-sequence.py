class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [-1] * (2 * n - 1)
        started = set()
        
        def backtrack(index: int) -> int:
            if index == 2 * n - 1:
                return True
            if seq[index] != -1:
                return backtrack(index + 1)
            
            for i in range(n, 0, -1):
                if i in started:
                    continue
                if i != 1 and index + i >= len(seq):
                    return False
                if i != 1 and seq[index + i] != -1:
                    continue
                seq[index] = i
                if i != 1:
                    seq[index + i] = i
                started.add(i)
                if backtrack(index + 1):
                    return True
                started.remove(i)
                if i != 1:
                    seq[index + i] = -1
                seq[index] = -1
                    
            return False
        
        backtrack(0)
        return seq