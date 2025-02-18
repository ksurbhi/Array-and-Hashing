class Solution:
  # Method1: Bruit Force with time comp = O(n*klogk)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      my_dict = defaultdict(list)
      for s in strs:
        sorted_s = '.'join(sorted(s))
        my_dict[sorted_s].append(s)
      return list(my_dict.values())
      
    # Method 2: Optimal one with time comp = O(n*k)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      my_dict = defaultdict(list)
      for s in strs:
        count = [0]*26
        for c in s:
          askii = ord(c)-ord('a')
          count[askii] += 1
        key = tuple(count)
        my_dict[key].append(s)
      return list(my_dict.values())
        


                    
  
