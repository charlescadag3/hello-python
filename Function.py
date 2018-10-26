# def sayhello (name, school = "CSNHS"):
#     print("hello, {} from {}!".format(name,school))

# sayhello("Charles")
# sayhello("Charles", "CSNHS")
# sayhello(name="Charlesu",school="CSNHS1")
# sayhello(school="NCS1", name="Charles")

# def sorted([2,4,6,1,3,5]):
#     print (sorted())
#bin(4)


# def square(x):
#     return x*x
# for y in range(10):
#     print("{}**2 == {}"
#     .format(y,square(y)))


UserIn = input("Enter a comma separated list of numbers :")
values =UserIn.split(",")
total = 0.0
for i in range (len(values)):
    g = float(values[i])
total += g*g
print("The sum of the square:"+str(total))
#print (total)

