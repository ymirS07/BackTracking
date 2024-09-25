class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking(startIndex, nums, path):
            res.append(path[:])
            if startIndex == len(nums):
                return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtracking(i+1, nums, path)
                path.pop()
        backtracking(0, nums, path)
        return res
# 不用copy，速度起飞
    
