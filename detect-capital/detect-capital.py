class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppers = [c for c in word if c.isupper()]
    
        if len(uppers) == 0:
            return True

        if len(word) == len(uppers):
            return True
        else:
            return len(uppers) == 1 and word[0].isupper()
                             
        