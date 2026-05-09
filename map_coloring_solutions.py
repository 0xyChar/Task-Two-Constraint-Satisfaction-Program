# Australia Map Coloring - 5 regions using 3 colors
from constraint import Problem, AllDifferentConstraint

def australia_coloring():
    """
    Color Australian states/territories using 3 colors
    No two adjacent states share the same color
    """
    
    # Define the regions
    regions = ['Western_Australia', 'Northern_Territory', 'Queensland', 
               'South_Australia', 'New_South_Wales']
    
    # Define adjacency (neighbors)
    # Each tuple represents adjacent regions
    adjacent_pairs = [
        ('Western_Australia', 'Northern_Territory'),
        ('Western_Australia', 'South_Australia'),
        ('Northern_Territory', 'Queensland'),
        ('Northern_Territory', 'South_Australia'),
        ('Queensland', 'South_Australia'),
        ('Queensland', 'New_South_Wales'),
        ('South_Australia', 'New_South_Wales'),
        ('New_South_Wales', 'South_Australia')
    ]
    
    # Available colors
    colors = ['Blue', 'Red', 'Green']
    
    # Create problem instance
    problem = Problem()
    
    # Add variables (regions) with their domains (colors)
    for region in regions:
        problem.addVariable(region, colors)
    
    # Add constraints: adjacent regions must have different colors
    for region1, region2 in adjacent_pairs:
        problem.addConstraint(lambda x, y: x != y, (region1, region2))
    
    # Find all solutions
    solutions = problem.getSolutions()
    
    # Display results
    print("="*60)
    print("Task (a): Australia Map Coloring (5 regions - 3 colors)")
    print("="*60)
    print(f"Total number of solutions found: {len(solutions)}\n")
    
    # Display first 5 solutions
    print("First 5 solutions:")
    for i, solution in enumerate(solutions[:5], 1):
        print(f"\nSolution {i}:")
        for region, color in solution.items():
            print(f"  {region}: {color}")
    
    # Verify a valid coloring
    if solutions:
        print("\n✓ Valid coloring achieved!")
        print("All adjacent regions have different colors.")
        
        # Display adjacency verification for first solution
        print("\nAdjacency verification for Solution 1:")
        for region1, region2 in adjacent_pairs:
            print(f"  {region1}({solutions[0][region1]}) vs {region2}({solutions[0][region2]}) ✓")
    
    return solutions

def visualize_australia_coloring(solution):
    """Simple visualization of the coloring"""
    print("\n" + "="*60)
    print("Visual Representation:")
    print("="*60)
    
    # Group colors
    color_groups = {'Blue': [], 'Red': [], 'Green': []}
    for region, color in solution.items():
        color_groups[color].append(region)
    
    for color in ['Blue', 'Red', 'Green']:
        print(f"\n{color}: {', '.join(color_groups[color])}")

# Run the Australia coloring
if __name__ == "__main__":
    solutions = australia_coloring()
    if solutions:
        visualize_australia_coloring(solutions[0])
