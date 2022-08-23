class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        
        while n != 1:
            n = sum([int(x) ** 2 for x in str(n)])

            if n in nums:
                return False
            
            nums.add(n)
        
        return True