class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(nlogn)
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
# Method 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using hashmap O(n)
        if len(s) != len(t):
            return False
        t_map={}
        s_map={}
        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i],0)
            t_map[t[i]] =  1+t_map.get(t[i],0)
        return s_map == t_map

  #method 3
  class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using hashmap but efficiently 
        # Time Comp: O(n)
        if len(s) != len(t):
            return False
        count =[0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] +=1
            count[ord(t[i])-ord('a')] -=1
        for val in count:
            if val != 0:
                return False
        return True
