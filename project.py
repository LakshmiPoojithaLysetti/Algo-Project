def find_starting_city(city_distances, fuel, mpg):
    total_cities = len(city_distances)
    
    for start_city in range(total_cities):
        remaining_fuel = 0
        current_city = start_city
        can_complete_journey = True
        
        for _ in range(total_cities):
            remaining_fuel += fuel[current_city] * mpg - city_distances[current_city]
            
            if remaining_fuel < 0:
                can_complete_journey = False
                break
            
            current_city = (current_city + 1) % total_cities
        
        if can_complete_journey:
            return start_city
    
    return -1  # No valid starting city found

# Sample Input
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Output
print(find_starting_city(city_distances, fuel, mpg))  # Output: 4
