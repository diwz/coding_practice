# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candyNum = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candyNum[i] = candyNum[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candyNum[i] <= candyNum[i+1]:
                candyNum[i] = candyNum[i+1] + 1

        return candyNum
