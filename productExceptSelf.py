class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Space: O(N) EX: [1,2,3,4] ---> [24,12,8,6]
        # Time : O(N)
      #[1,1,2,6]
      #[24,12,4,1]
      l = 0
      n = len(nums)
      r = n-1
      right_prod, left_prod, result = [1]*n ,[1]*n,[1]*n
      for i in range(1,n):
        left_prod[i] = left_prod[i-1]*nums[i-1]
      for i in range(n-2,-1,-1):
        right_prod[i] = right_prod[i+1]*nums[i+1]
      for i in range(n):
        res[i] = left_prod[i]*right_prod[i]
      return res


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Space: O(N) EX: [1,2,3,4] ---> [24,12,8,6]
        # Time : O(N)
      #[1,1,2,6]
      #[24,12,4,1]
      left_prod = 1
      right_prod =1
      l =0
      r = len(nums)-1
      res = [1]*len(nums)
      while l< len(nums) and r > -1:
        res[l] = res[l]*left_prod
        res[r] = res[r]*right_prod
        left_prod = left_prod*nums[l]
        right_prod = right_prod * nums[r]
        l += 1
        r -=1
      return res
        
        
        
        
        
        
      
        
