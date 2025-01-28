class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n*n)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
#Method 2
class Solution:
    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for key,value in enumerate(nums):
            diff = target-value
            if diff in my_map:
                return [my_map[diff],key]
            my_map[value] = key
