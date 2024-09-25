class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums = sorted(nums)
        def backtracking(startIndex, path, nums):
            res.append(path[:])
            uset = set()
            if startIndex == len(nums):
                return
            for i in range(startIndex, len(nums)):
                if nums[i] in uset:
                    continue
                uset.add(nums[i])
                path.append(nums[i])
                backtracking(i + 1, path, nums)
                path.pop()
        backtracking(0, path, nums)
        return res

# 用set判断每一层的重复
