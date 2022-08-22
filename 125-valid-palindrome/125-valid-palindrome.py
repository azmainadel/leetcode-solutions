class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_filtered = []
        
        # for c in s:
        #     if c.isalnum():
        #         s_filtered.append(c.lower())
        
        s_filtered = [c.lower() for c in s if c.isalnum()]
        
        return s_filtered == s_filtered[::-1]