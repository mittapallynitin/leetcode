class Solution:
    def candy(self, ratings: List[int]) -> int:
        kids = len(ratings)
        total_candies = [1]*kids
        for i in range(1, kids):
            if (ratings[i-1] < ratings[i]) and (total_candies[i] <= total_candies[i-1]):
                total_candies[i] = total_candies[i-1] + 1
        for i in range(kids-2, -1, -1):
            if (ratings[i+1] < ratings[i]) and (total_candies[i] <= total_candies[i+1]):
                total_candies[i] = total_candies[i+1] + 1
        return sum(total_candies)



        