class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            remaining = target - nums[i]
            
            if remaining in hashmap and hashmap[remaining] != i:
                return [i, hashmap[remaining]]