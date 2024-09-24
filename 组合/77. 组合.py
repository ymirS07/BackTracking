class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(startIndex, path):
            if len(path) == k:
                res.append(path.copy())
                return
            max_edge = n - (k - len(path)) + 1
            for i in range(startIndex, n - (k - len(path)) + 1):
                path.append(i+1)
                backtracking(i+1, path)
                path.pop()
        backtracking(0, path)
        return res


#剪枝：当剩余数的个数不够时。
