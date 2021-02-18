class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        
        output = ''
        for word in words:
            output += (' ' + word)
            
        return output.strip()