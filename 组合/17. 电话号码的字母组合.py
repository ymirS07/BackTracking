class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        key_board = {"0":"", "1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        path = []
        def backtracking(startIndex, digits):
            if len(path) == len(digits):
                res.append("".join(path.copy()))
                return
            for i in range(startIndex, len(digits) - (len(digits) - len(path)) + 1):
                for letter in key_board[digits[i]]:
                    path.append(letter)
                    backtracking(i + 1, digits)
                    path.pop()
        backtracking(0, digits)
        return res

