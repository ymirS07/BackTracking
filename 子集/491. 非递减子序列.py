class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking(nums, starIndex):
            if len(path) > 1:
                res.append(path.copy())
            uset = set()
            for i in range(starIndex, len(nums)):
                if nums[i] in uset or (path and nums[i] < path[-1]):
                    continue
                uset.add(nums[i])
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()
        backtracking(nums, 0)
        return res
