class Solution:
    def romanToInt(self, s: str) -> int:
        romanValueMap = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000,
        }
        
        result = 0
        left = 1000
        
        for c in s:
            current = romanValueMap[c]
            result += current
            
            if left < current:
                result -= left*2
                
            left = current
            
        return result