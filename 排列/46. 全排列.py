class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = [False] * len(nums)
        def backtracking(path, nums, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtracking(path, nums, visited)
                visited[i] = False
                path.pop()
        backtracking(path, nums, visited)
        return res
# 控制纵向的不重复选
