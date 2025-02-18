class Solution:
  # Time Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict()
        for num in nums:
            freq_map[num]= 1+freq_map.get(num,0)
        print(freq_map)
        heap = []
        for key,freq in freq_map.items():
            heapq.heappush(heap,(freq,key))
            if len(heap) >k:
                heapq.heappop(heap)
        return [value[1] for value in heap]
