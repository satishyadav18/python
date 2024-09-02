# Take user input for the length and breadth of a rectangle
length_rectangle = float(input("Enter the length of the rectangle: "))
breadth_rectangle = float(input("Enter the breadth of the rectangle: "))

# Take user input for the radius of a circle
radius_circle = float(input("Enter the radius of the circle: "))

# Calculate perimeter and area of the rectangle
perimeter_rectangle = 2 * (length_rectangle + breadth_rectangle)
area_rectangle = length_rectangle * breadth_rectangle

# Calculate circumference and area of the circle
circumference_circle = 2 * 3.14 * radius_circle
area_circle = 3.14 * radius_circle**2

# Print the results
print("\nRectangle:")
print(f"Perimeter: {perimeter_rectangle}")
print(f"Area: {area_rectangle}")

print("\nCircle:")
print(f"Circumference: {circumference_circle}")
print(f"Area: {area_circle}")
