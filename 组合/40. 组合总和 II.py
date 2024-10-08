class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def backtracking(candidates, target, startindex):
            if target < 0:
                return
            if target == 0:
                p = path.copy()
                res.append(p)
                return
            for i in range(startindex, len(candidates)):
                if i > startindex and candidates[i] == candidates[i-1]:
                    continue
                if target - candidates[i] < 0:
                    break
                path.append(candidates[i])
                target -= candidates[i]
                backtracking(candidates, target, i+1)
                target += candidates[i]
                path.pop()

        backtracking(candidates, target, 0)
        return res
#剪枝：需要先把数组变成有序的，同一层不允许重复，那么就是需要同时满足i > startindex and candidates[i] == candidates[i-1]
