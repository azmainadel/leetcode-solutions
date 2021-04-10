class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        values1 = version1.split('.')
        values2 = version2.split('.')
        
        while values1 or values2:
            n1 = int(values1.pop(0)) if values1 else 0
            n2 = int(values2.pop(0)) if values2 else 0
            
            if n1 > n2:
                return 1
            elif n2 > n1:
                return -1
        
        return 0
        