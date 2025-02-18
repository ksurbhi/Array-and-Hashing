class Solution:
  # Time Complexity: O(n)
    def encode(self, strs: List[str]) -> str:
        res= ""
        for s in strs:
            res += str(len(s)) +'#'+s
        return res

    #res = 4#neet4#code
    def decode(self, s: str) -> List[str]:
      result = []
      i = 0
      while i < len(s):
        j = i
        while s[j] != '#':
          j = j+1
        length = int(s[i:j])
        word = s[j+1:j+1+length]
        result.append(word)
        i = j+1+length
      return result
        
