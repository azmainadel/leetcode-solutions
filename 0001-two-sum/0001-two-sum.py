class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i in range(len(nums)):
            remaining = target - nums[i]
            
            if remaining in hashMap:
                return [i, hashMap[remaining]]
            else:
                hashMap[nums[i]] = i
        