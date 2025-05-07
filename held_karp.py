import itertools

def tsp_held_karp(distances, cities):
    """
    Solves the Traveling Salesman Problem (TSP) using the Held-Karp algorithm 
    (dynamic programming with bitmasking).
    
    Approach:
    - Use bitmasking to represent subsets of cities.
    - Use recursion with memoization to compute the shortest path to a given city 
      while keeping track of visited cities.
    - Reconstruct the path after finding the minimum cost tour.

    Complexity:
    - Time Complexity: O(n^2 * 2^n), where `n` is the number of cities.
    - Space Complexity: O(n * 2^n) due to memoization storage.
    
    Parameters:
    - distances: 2D list where distances[i][j] represents the travel cost from city `i` to `j`.
    - cities: Dictionary mapping city names to their index in `distances`.

    Returns:
    - min_tour_length: The minimum possible distance for the optimal tour.
    - tour: List of city indices representing the shortest tour.
    """

    start_city = cities['los_angeles']
    n = len(distances)

    # Memoization table to store minimum distance to visit a subset of cities ending at `last`
    memo = {}
    prev = {}

    def dp(mask, last):
        """
        Recursively computes the minimum cost path to visit the subset of cities 
        represented by `mask`, ending at city `last`.
        """
        # Base case: If only the start city is visited, cost is 0
        if mask == (1 << start_city) and last == start_city:
            return 0  

        # If result is already computed, return it from memoization
        if (mask, last) in memo:
            return memo[(mask, last)]
        
        min_dist = float('inf')
        best_prev = None

        # Try visiting all cities in the subset except `last`
        for city in range(n):
            if city != last and (mask & (1 << city)):  # If `city` is in the subset
                new_mask = mask ^ (1 << last)  # Remove `last` from subset
                dist = dp(new_mask, city) + distances[city][last]  # Compute distance

                # Update minimum distance and the best previous city
                if dist < min_dist:
                    min_dist = dist
                    best_prev = city
        
        # Store the best computed distance in memoization table
        memo[(mask, last)] = min_dist
        prev[(mask, last)] = best_prev  # Store best previous city for reconstruction
        return min_dist

    # Find the shortest tour length by trying all possible end cities
    min_tour_length = float('inf')
    best_city = None

    for city in range(n):
        if city != start_city:
            # Compute cost of reaching `city` and returning to start
            tour_length = dp((1 << n) - 1, city) + distances[city][start_city]
            if tour_length < min_tour_length:
                min_tour_length = tour_length
                best_city = city

    # Reconstruct the shortest tour from `prev` dictionary
    tour = [start_city]  # Start from the initial city
    mask = (1 << n) - 1
    city = best_city

    while city is not None:
        tour.append(city)
        next_city = prev.get((mask, city), None)  # Get previous city in optimal path
        mask ^= (1 << city)  # Remove city from visited set
        city = next_city

    tour.append(start_city)  # Close the loop

    return min_tour_length, tour

# City index mapping
cities = {
    "new_york": 0,
    "tel_aviv": 1,
    "rome": 2,
    "los_angeles": 3,
    "lima": 4,
    "dubai": 5,
    "tokio": 6,
    "venice": 7,
    "london": 8
}

# Distance matrix representing travel costs between cities
distances = [
    [0, 600, 800, 1200, 1500, 1200, 1500, 1000, 800],  # new_york
    [600, 0, 400, 1000, 1300, 900, 1100, 800, 700],     # tel_aviv
    [800, 400, 0, 700, 1000, 600, 900, 500, 600],      # rome
    [1200, 1000, 700, 0, 500, 900, 1200, 1100, 900],   # los_angeles
    [1500, 1300, 1000, 500, 0, 800, 1400, 1200, 1100], # lima
    [1200, 900, 600, 900, 800, 0, 1200, 1000, 700],    # dubai
    [1500, 1100, 900, 1200, 1400, 1200, 0, 1300, 1200],# tokio
    [1000, 800, 500, 1100, 1200, 1000, 1300, 0, 400],  # venice
    [800, 700, 600, 900, 1100, 700, 1200, 400, 0]      # london
]

# Run the TSP solver
min_distance, shortest_tour = tsp_held_karp(distances, cities)

# Convert tour indices to city names
f_tour = [city_name for city in shortest_tour for city_name, index in cities.items() if index == city]

# Output the results
print("Minimum distance:", min_distance)
print("Shortest tour:", f_tour)
