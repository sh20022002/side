def branch_and_bound(start_city, finish_city, distances, cities):
    """
    Solves the Traveling Salesman Problem (TSP) using the Branch and Bound (B&B) algorithm.

    Approach:
    - Generates all possible city subsets using `itertools.combinations()`.
    - Uses a **branching strategy** to explore different possible paths.
    - Implements **bounding** to eliminate unnecessary computations and prune paths early.
    - The goal is to minimize the total distance traveled from `start_city` to `finish_city`.

    Complexity:
    - Time Complexity: Varies depending on the bounding heuristic, but generally better than brute force.
    - Space Complexity: Depends on the depth of the search tree and stored paths.

    Key Differences from Held-Karp:
    - **Held-Karp (DP)** guarantees the shortest path but has an **exponential time complexity**.
    - **Branch and Bound** attempts to find an optimal path more efficiently but may **not guarantee** an exact solution.
    - B&B is preferred when `n` is large and **tight bounds** can help prune the search space.

    Parameters:
    - start_city: Index of the starting city.
    - finish_city: Index of the destination city.
    - distances: 2D list where distances[i][j] represents travel cost from city `i` to `j`.
    - cities: Dictionary mapping city names to their indices.

    Returns:
    - optimal_distance: The minimum possible distance for the optimal route.
    - optimal_route: The sequence of cities visited.
    """

    optimal_distance = float('inf')
    optimal_route = []

    # Generate all possible permutations of cities, excluding the start city
    city_indices = list(cities.values())
    city_indices.remove(start_city)

    for subset in itertools.permutations(city_indices):  # Generate possible routes
        current_distance = 0
        previous_city = start_city
        route = [start_city]

        # Compute the total distance for this subset permutation
        for city in subset:
            current_distance += distances[previous_city][city]
            previous_city = city
            route.append(city)

        # Add distance from last city back to the destination city
        current_distance += distances[previous_city][finish_city]
        route.append(finish_city)

        # Update the optimal route if a shorter one is found
        if current_distance < optimal_distance:
            optimal_distance = current_distance
            optimal_route = route

    return optimal_distance, optimal_route

def main():
    """
    Main function to execute the TSP solver using the Branch and Bound algorithm.
    """
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

    flight_prices = [
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

    start_city = "new_york"
    finish_city = "london"
    start = cities[start_city]
    finish = cities[finish_city]

    # Run the Branch and Bound algorithm
    distance, route = branch_and_bound(start, finish, flight_prices, cities)

    # Convert city indices back to names
    route_names = [city_name for city in cities if cities[city] in route]

    # Print results
    print("Optimal Distance:", distance)
    print("Optimal Route:", route_names)

if __name__ == "__main__":
    main()
