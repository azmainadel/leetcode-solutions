class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        return haystack.index(needle) if haystack.count(needle) > 0 else -1