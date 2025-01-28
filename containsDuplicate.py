class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n*n)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

  #Method 2:
  class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # O(nlogn)
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False
# Method 3
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) Using set
        my_set = set()
        for num in nums:
            my_set.add(num)
        if len(nums)!= len(my_set):
            return True
        return False

