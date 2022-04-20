class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        
        for number in nums:
            if number in seen:
                seen.remove(number)
            else:
                seen.add(number)
        
        return seen.pop()
                