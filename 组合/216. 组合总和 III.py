class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(startIndex, n):
            if len(path) == k:
                if n == 0:
                    res.append(path.copy())
                return
                
            for i in range(startIndex, 9):
                n -= (i + 1)
                if n < 0:
                    return
                path.append(i + 1)
                backtracking(i + 1, n)
                n += (i + 1)
                path.pop()
        backtracking(0, n)
        return res

#剪枝：当和超过n时。
