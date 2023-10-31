import os

def flood_fill(plane, x, y, replacement_color):
    target_color = plane.plane[plane.size - y - 1][x].value
    if target_color == replacement_color:
        return  # Nothing to do if the target color is the same as the replacement color

    def _flood_fill_recursive(x, y):
        if (
            0 <= plane.size - y - 1 < plane.size and
            0 <= x < plane.size and
            plane.plane[plane.size - y - 1][x].value == target_color
        ):
            # Set the new color at the current position
            plane.plane[plane.size - y - 1][x].value = replacement_color

            # Display the updated plane
            os.system('cls' if os.name == 'nt' else 'clear')
            plane.print("Progress:")
            
            # Recursively call flood_fill on neighboring pixels
            _flood_fill_recursive(x + 1, y)  # Right
            _flood_fill_recursive(x - 1, y)  # Left
            _flood_fill_recursive(x, y + 1)  # Down
            _flood_fill_recursive(x, y - 1)  # Up

    # Start the flood fill and display the initial state
    plane.print("Initial State:")
    _flood_fill_recursive(x, y)
    plane.print("Final State:")
