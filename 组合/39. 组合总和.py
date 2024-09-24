class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(startIndex, candidates, target):
            if target < 0:
                return
            if target == 0:
                res.append(path.copy())
                return
            for i in range(startIndex, len(candidates)):
                path.append(candidates[i])
                target -= candidates[i]
                backtracking(i, candidates, target)
                target += candidates[i]
                path.pop()
        backtracking(0, candidates, target)
        return res
#剪枝：注意这里剪枝的位置，以及startIndex为什么还是需要！
