class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        def isPalindrome(sub_s):
            if len(sub_s) == 1:
                return True
            left, right = 0, len(sub_s) - 1
            while left < right:
                if sub_s[left] != sub_s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtracking(startIndex, s, path):
            if startIndex == len(s):
                res.append(path.copy())
                return
            for i in range(startIndex, len(s)):
                sub_s = s[startIndex:i + 1]
                if isPalindrome(sub_s):
                    path.append(sub_s)
                    backtracking(i+1, s, path)
                    path.pop()
        backtracking(0, s, path)
        return res

# 注意如何把组合问题转变为分割问题
# 剪枝：是回文
# 终止：纵向走到头
