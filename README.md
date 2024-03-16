# Finding Preferred Starting City
## Problem Statement:
Given a circular layout of cities, each with a gas station that provides a specified amount of fuel, and the distances between surrounding cities, the task is to discover the ideal beginning city. The objective is to begin in one city, travel to every other city, and end up back in the beginning city with at least zero gallons of petrol remaining.

## Approach:
### 1) Calculate Fuel Required:
Calculate the total distance the circular route will need to go as you pass through the cities.To calculate the entire amount of fuel needed to finish the trip, divide the whole distance by the car's fuel efficiency (miles per gallon).

### 2) Check Feasible Starting Cities:
- Calculate the cumulative gas available beginning in each city as you go through them.
- Also see if there is enough gas to cover the entire amount.

### 3)fuel required.
- It is not possible to begin from any city if the cumulative gas there turns negative.
- Monitor the final city's index where the cumulative gas is still positive.

### 4)Return Preferred Starting City:
The ideal starting city is the index of the final city where the cumulative gas is still non-negative.

## Implementation:
### Input:
1) D (city_distances): Array representing distances between neighboring cities.
2) F (fuel): Array representing the amount of gas available at each city.
3) mpg: Miles per gallon, representing the car's fuel efficiency.

### Output:
Index of the preferred starting city.

## Algorithm: 
1) Determine the total amount of fuel used by multiplying the mileage driven by the car's MPG.
2) Calculate the total amount of gas available starting from each city as you iterate through them.
3) Find the final city in which the cumulative gas balance is positive.
4) Give back the starting city's desired index.

## Complexity Analysis:
- Time Complexity: O(n^2), where n is the number of cities.
- Space Complexity: O(1).

## Usage: 
- Enter the following input parameters: mpg, fuel, and city_distances.
- Use the given parameters to invoke the findPreferredStartingCity function.
- As the output, get the index of the desired beginning city.

