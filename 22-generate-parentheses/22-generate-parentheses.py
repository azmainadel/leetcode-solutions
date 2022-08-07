class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []
        
        def dfs(leftRemaining, rightRemaining, currentSolution):
            if leftRemaining > rightRemaining or leftRemaining < 0 or rightRemaining < 0:
                return
            
            if rightRemaining == 0:
                solutions.append(currentSolution)
                return
            
            dfs(leftRemaining - 1, rightRemaining, currentSolution + "(")
            dfs(leftRemaining, rightRemaining - 1, currentSolution + ")")
            
        dfs(n, n, "")
        return solutions