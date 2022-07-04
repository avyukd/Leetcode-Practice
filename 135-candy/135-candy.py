class Solution:
    def candy(self, ratings: List[int]) -> int:
        if (ratings == sorted(ratings) or ratings == sorted(ratings, reverse=True)) and len(ratings) == len(set(ratings)):
            n = len(ratings)
            return (int) ( (n * (n + 1)) / 2 )
        
        candies = [1] * len(ratings)
        # attempt 1 - forward pass, backward pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = 1 + candies[i - 1]
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                while candies[i] <= candies[i + 1]:
                    candies[i] += 1
        
        return sum(candies)
