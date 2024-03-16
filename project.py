def find_starting_city(D, F, mpg): 
#'TC' be the total number of cities 
    TC = len(D) 
    
# 'SC' be the start city 
    for SC in range(TC):    

        fuel_left = 0 
# 'CC' being the current city is equal to start city 
        CC = SC   
        can_complete_journey = True 
        for _ in range(TC): 
            fuel_left += F[CC] * mpg - D[CC] 
            if fuel_left < 0: 
                can_complete_journey = False 
                break 
                
            CC = (CC + 1) % TC 

        if can_complete_journey: 
            return SC 
# No valid starting city found     

    return -1   


# Sample Input 
D = [5, 25, 15, 10, 15] 
F = [1, 2, 1, 0, 3] 
mpg = 10 

# Output 
print(find_starting_city(D, F, mpg))  # Output: 4 
