class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rateMap = {foods[i]: ratings[i] for i in range(len(foods))}
        self.foodMap = {foods[i]: cuisines[i] for i in range(len(foods))}
        self.cuisineMap = {i: [] for i in cuisines}
        for i in range(len(foods)):
            heappush(self.cuisineMap[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.rateMap[food] = newRating
        cuisine = self.foodMap[food]
        heappush(self.cuisineMap[cuisine], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        while self.cuisineMap[cuisine][0][0] != -self.rateMap[self.cuisineMap[cuisine][0][1]]:
            heappop(self.cuisineMap[cuisine])
        return self.cuisineMap[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)