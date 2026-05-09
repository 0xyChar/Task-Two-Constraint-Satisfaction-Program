# Nairobi Sub-counties Coloring - Minimizing number of colors
from constraint import Problem
import itertools

class NairobiColoring:
    """
    Color Nairobi's 17 sub-counties with minimum number of colors
    """
    
    def __init__(self):
        # Define Nairobi's 17 sub-counties
        self.sub_counties = [
            'Westlands', 'Dagoretti North', 'Dagoretti South', 'Langata', 
            'Kibra', 'Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi North',
            'Embakasi South', 'Embakasi Central', 'Embakasi East', 
            'Embakasi West', 'Makadara', 'Kamukunji', 'Starehe', 'Mathare'
        ]
        
        # Define adjacency based on actual Nairobi geography
        # This is a simplified but realistic adjacency matrix
        self.adjacency_pairs = self.create_adjacency_pairs()
        
    def create_adjacency_pairs(self):
        """
        Create adjacency relationships between sub-counties
        Based on actual Nairobi administrative boundaries
        """
        adj_pairs = [
            # Central & Western areas
            ('Westlands', 'Dagoretti North'),
            ('Westlands', 'Kibra'),
            ('Westlands', 'Starehe'),
            ('Dagoretti North', 'Dagoretti South'),
            ('Dagoretti North', 'Westlands'),
            ('Dagoretti South', 'Langata'),
            ('Dagoretti South', 'Kibra'),
            ('Langata', 'Kibra'),
            ('Langata', 'Embakasi West'),
            ('Kibra', 'Dagoretti North'),
            ('Kibra', 'Langata'),
            ('Kibra', 'Starehe'),
            
            # Eastern areas
            ('Roysambu', 'Kasarani'),
            ('Roysambu', 'Embakasi North'),
            ('Kasarani', 'Ruaraka'),
            ('Kasarani', 'Embakasi North'),
            ('Ruaraka', 'Embakasi North'),
            ('Ruaraka', 'Mathare'),
            ('Embakasi North', 'Embakasi Central'),
            ('Embakasi North', 'Roysambu'),
            ('Embakasi Central', 'Embakasi South'),
            ('Embakasi Central', 'Embakasi East'),
            ('Embakasi South', 'Embakasi Central'),
            ('Embakasi South', 'Makadara'),
            ('Embakasi East', 'Embakasi Central'),
            ('Embakasi East', 'Embakasi West'),
            ('Embakasi West', 'Langata'),
            ('Embakasi West', 'Makadara'),
            ('Embakasi West', 'Embakasi East'),
            
            # Central areas
            ('Makadara', 'Embakasi West'),
            ('Makadara', 'Embakasi South'),
            ('Makadara', 'Starehe'),
            ('Kamukunji', 'Starehe'),
            ('Kamukunji', 'Mathare'),
            ('Kamukunji', 'Makadara'),
            ('Starehe', 'Westlands'),
            ('Starehe', 'Kibra'),
            ('Starehe', 'Makadara'),
            ('Starehe', 'Kamukunji'),
            ('Mathare', 'Starehe'),
            ('Mathare', 'Kamukunji'),
            ('Mathare', 'Ruaraka'),
            
            # Additional adjacencies
            ('Dagoretti North', 'Kasarani'),  # Northern connection
            ('Roysambu', 'Westlands'),  # Western-Eastern link
            ('Mathare', 'Embakasi North'),  # Northern-Eastern link
        ]
        
        # Remove duplicates by converting to set and back to list
        unique_pairs = set()
        for r1, r2 in adj_pairs:
            # Ensure consistent ordering (smaller index first)
            if r1 < r2:
                unique_pairs.add((r1, r2))
            else:
                unique_pairs.add((r2, r1))
        
        return list(unique_pairs)
    
    def find_minimum_colors(self):
        """
        Find the minimum number of colors needed to color Nairobi sub-counties
        """
        # Try with 2, 3, 4 colors until a solution is found
        print("="*60)
        print("Task (b): Nairobi Sub-counties Coloring")
        print("="*60)
        print(f"Number of sub-counties: {len(self.sub_counties)}")
        print(f"Number of adjacent pairs: {len(self.adjacency_pairs)}")
        print("\nFinding minimum colors required...")
        
        for num_colors in range(2, 6):
            print(f"\nTrying with {num_colors} colors...")
            solution = self.solve_with_colors(num_colors)
            if solution:
                print(f"\n✓ SUCCESS! Minimum colors required: {num_colors}")
                return solution, num_colors
        
        print("\n✗ Could not find solution with up to 5 colors")
        return None, 0
    
    def solve_with_colors(self, num_colors):
        """
        Attempt to solve coloring with given number of colors
        """
        # Create generic color names
        colors = [f'Color_{i+1}' for i in range(num_colors)]
        
        # Create problem
        problem = Problem()
        
        # Add variables
        for sub_county in self.sub_counties:
            problem.addVariable(sub_county, colors)
        
        # Add constraints
        for region1, region2 in self.adjacency_pairs:
            problem.addConstraint(lambda x, y: x != y, (region1, region2))
        
        # Get a single solution
        solutions = problem.getSolutions()
        
        if solutions:
            return solutions[0]
        return None
    
    def display_coloring(self, solution, num_colors):
        """
        Display the coloring results
        """
        print("\n" + "="*60)
        print(f"Coloring Solution for Nairobi Sub-counties ({num_colors} colors)")
        print("="*60)
        
        # Group by color
        color_map = {}
        for sub_county, color in solution.items():
            if color not in color_map:
                color_map[color] = []
            color_map[color].append(sub_county)
        
        # Display color groups
        for i, (color, sub_counties_list) in enumerate(color_map.items(), 1):
            print(f"\n{color}:")
            # Display sub-counties in rows of 5 for better readability
            for j in range(0, len(sub_counties_list), 5):
                print(f"  {', '.join(sub_counties_list[j:j+5])}")
        
        print(f"\nTotal sub-counties colored: {len(solution)}")
        print(f"Colors used: {list(color_map.keys())}")
        
        # Verify constraints
        self.verify_solution(solution)
    
    def verify_solution(self, solution):
        """
        Verify that all constraints are satisfied
        """
        print("\n" + "="*60)
        print("Verification:")
        print("="*60)
        
        violations = []
        for region1, region2 in self.adjacency_pairs:
            if solution[region1] == solution[region2]:
                violations.append((region1, region2, solution[region1]))
        
        if violations:
            print(f"✗ Found {len(violations)} violations:")
            for r1, r2, color in violations[:10]:  # Show first 10 violations
                print(f"  {r1} and {r2} both have {color}")
        else:
            print("✓ All constraints satisfied! No adjacent sub-counties share the same color.")
    
    def get_statistics(self):
        """
        Display statistics about the problem
        """
        # Calculate degree of each sub-county
        degree = {sc: 0 for sc in self.sub_counties}
        for r1, r2 in self.adjacency_pairs:
            degree[r1] += 1
            degree[r2] += 1
        
        print("\n" + "="*60)
        print("Problem Statistics:")
        print("="*60)
        print(f"Number of sub-counties: {len(self.sub_counties)}")
        print(f"Number of adjacency relationships: {len(self.adjacency_pairs)}")
        print("\nHighest degree sub-counties (most neighbors):")
        
        # Sort by degree
        sorted_degrees = sorted(degree.items(), key=lambda x: x[1], reverse=True)
        for i, (sc, deg) in enumerate(sorted_degrees[:5], 1):
            print(f"  {i}. {sc}: {deg} neighbors")
        
        # Lower bound calculation (chromatic number lower bound)
        max_degree = max(degree.values())
        lower_bound = max_degree + 1
        print(f"\nTheoretical lower bound (≥ max_degree+1): {lower_bound} colors")

# Run Nairobi coloring
if __name__ == "__main__":
    # Create Nairobi coloring instance
    nairobi = NairobiColoring()
    
    # Display statistics
    nairobi.get_statistics()
    
    # Find minimum coloring
    solution, num_colors = nairobi.find_minimum_colors()
    
    # Display results
    if solution:
        nairobi.display_coloring(solution, num_colors)
        
        # Optional: Create a simple text-based map representation
        print("\n" + "="*60)
        print("Text-based Map Representation:")
        print("="*60)
        print("\nColor Legend:")
        for color in set(solution.values()):
            print(f"  {color}")
        
        print("\nRegional Grouping:")
        # Group by geographical area
        western = ['Westlands', 'Dagoretti North', 'Dagoretti South', 'Langata', 'Kibra']
        central = ['Starehe', 'Kamukunji', 'Makadara', 'Mathare']
        eastern = ['Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi North', 'Embakasi South', 
                   'Embakasi Central', 'Embakasi East', 'Embakasi West']
        
        print("\nWestern Sub-counties:")
        for sc in western:
            print(f"  {sc}: {solution.get(sc, 'Unknown')}")
        
        print("\nCentral Sub-counties:")
        for sc in central:
            print(f"  {sc}: {solution.get(sc, 'Unknown')}")
        
        print("\nEastern Sub-counties:")
        for sc in eastern:
            print(f"  {sc}: {solution.get(sc, 'Unknown')}")
    else:
        print("\n✗ No solution found with reasonable number of colors")
