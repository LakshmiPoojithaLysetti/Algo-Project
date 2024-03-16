# Algorithm for Finding Preferred Starting City
Given a set of cities laid out in a circle, connected by a circular road, along with information about the distance between neighboring cities, the amount of gas available at each city, and the car's fuel efficiency (miles per gallon), the task is to design an algorithm to find the index of the preferred starting city. The preferred starting city is the one where you can start with an empty tank, visit all cities, and return back to the starting city with 0 or more gallons of fuel left.

## Approach:
### 1) Calculate Fuel Required:
Traverse through the cities and calculate the total distance to travel the circular road.
Divide the total distance by the car's fuel efficiency (miles per gallon) to determine the total fuel required to complete the journey.

### 2) Check Feasible Starting Cities:
Iterate through each city and calculate the cumulative gas available starting from that city and check if it's sufficient to cover the total

### 3)fuel required.
If at any city, the cumulative gas becomes negative, it means it's not feasible to start from that city.
Keep track of the index of the last city where the cumulative gas remains non-negative.

### 4)Return Preferred Starting City:
The index of the last city where the cumulative gas remains non-negative is the preferred starting city.

## Implementation:
### Input:
1) D (city_distances): Array representing distances between neighboring cities.
2) F (fuel): Array representing the amount of gas available at each city.
3) mpg: Miles per gallon, representing the car's fuel efficiency.

### Output:
Index of the preferred starting city.

## Algorithm:
1) Calculate total fuel required based on the total distance and car's MPG.
2) Iterate through cities, calculating cumulative gas available starting from each city.
3) Determine the last city where cumulative gas remains non-negative.
4) Return the index of the preferred starting city.

## Complexity Analysis:
Time Complexity: O(n), where n is the number of cities.
Space Complexity: O(1).

## Usage:
Provide input parameters: city_distances, fuel, and mpg.
Call the findPreferredStartingCity function with the input parameters.
Obtain the index of the preferred starting city as the output.
