class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        heap = heapq.nlargest(k, frequency.items(), key=lambda x: x[1])
        return [num for num, freq in heap]

