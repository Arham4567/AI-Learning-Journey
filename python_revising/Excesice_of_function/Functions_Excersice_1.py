#Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is (area = (1/2)*base*height)
#Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
def calculate_area(dimension1, dimension2,shape):
    if shape=="rectangle":
        area = dimension1*dimension2
        return area
    elif shape=="triangle":
        area = (1 / 2) * dimension1 * dimension2
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area = None
    return area

# Calculate area of triangle whose base is 10 and height is 5

triangle_area=calculate_area(4,2,"triangle")
print(triangle_area)

rectangle_area=calculate_area(4,2,"rectangle")
print(rectangle_area)