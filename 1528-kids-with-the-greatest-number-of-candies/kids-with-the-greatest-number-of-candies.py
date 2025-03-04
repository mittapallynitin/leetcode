class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= high)
        return result