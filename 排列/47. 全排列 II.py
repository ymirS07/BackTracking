class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums = sorted(nums)
        visited = [False]*len(nums)
        def backtracking(visited, path, nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                path.append(nums[i])
                backtracking(visited, path, nums)
                path.pop()
                visited[i] = False
        backtracking(visited, path, nums)
        return res
# 纵向去重，横向也要去重，重点关注后者！
