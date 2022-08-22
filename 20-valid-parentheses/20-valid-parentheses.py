class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_dict = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            if c not in p_dict:
                stack.append(c)
                continue
            if not stack or stack[-1] != p_dict[c]:
                return False
            stack.pop()
                
        return not stack
    