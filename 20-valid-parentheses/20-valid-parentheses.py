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

#     def isValid(self, s: str) -> bool:
#         stack = []
#         openParentheses = ['(', '{', '[']
#         closeParentheses = [')', '}', ']']

#         for c in s:
#             if c in openParentheses:
#                 stack.append(c)
#             else:
#                 if len(stack) != 0 and stack[-1] == openParentheses[closeParentheses.index(c)]:
#                     stack.pop()
#                 else:
#                     return False
#         return len(stack) == 0
