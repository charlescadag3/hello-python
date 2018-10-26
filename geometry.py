#import math

def triangle_perimeter (a,b,c):
  a+b+c
  return a+b+c


def triangle_heronsarea (a,b,c):

    s=(a+b+c)/2 
    A=((s*(s-a)*(s-b)*(s-c)))*(1/2) 
    return A 

if __name__ == "__main__":
    print("This is from geometry.py")

