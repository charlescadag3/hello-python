import geometry

def area_circle (radius):
    return math.pi * radius ** 2

data = input("Enter the radius of a circle: ")
radius =float(data)
print("Area of the circle: {:.4f}"
 .format(geometry.area_circle(radius)))


def area_circle (radius):
    return math.pi * radius ** 2

if _name_ == "_main_":
    print("This is from geometry.py")