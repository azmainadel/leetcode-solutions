class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magLetters = list(magazine)
        
        for c in ransomNote:
            if c not in magLetters:
                return False
            else:
                magLetters.remove(c)
        
        return True