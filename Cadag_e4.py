import geometry
def triangle_perimeter (a,b,c):
    
    return a+b+c


def triangle_heronsarea (a,b,c):
    s=(a+b+c)/2
    A=((s*(s-a)*(s-b)*(s-c)))*(1/2) 
    return A

# P = a+b+c
# s = (a+b+c)/2
# A = (s(s-a)(s-b)(s-c))


data = input("Enter the length value of a,b and c:(Use a comma) ")
triangle = data.split(",")
float(triangle) 


#print("Perimeter of a triangle: {}"/
 #.format(geometry.triangle_perimeter(P)))

