class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0
        
        for num in nums:
            if (num - 1) not in numSet:
                currentSeq = 0
                
                while (num + currentSeq) in numSet:
                    currentSeq += 1
                
                longestSeq = max(longestSeq, currentSeq)
        
        return longestSeq