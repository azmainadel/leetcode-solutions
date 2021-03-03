class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        try:
            result.append(nums.index(target))
        except ValueError:
            return [-1,-1]
        else:
            temp = nums[:]
            temp.reverse()
            result.append(len(nums) - temp.index(target) - 1)

            return result