# UserIn = input("Enter a comma separated list of numbers :")
# values =UserIn.split(",")
# print("The number you enter are{}".format(values[0],values[1],values[2],values[3],values[4])
# values = float(np.array(values[0],values[1],values[2],values[3],values[4]))
# values.astype(int)
# float(values)

# total = 0.0
# for i in range (len(values)):

# g = float(values[i])
# value1 =values[0] ** 2
# value2 =values[1] ** 2
# value3 =values[2] ** 2
# value4 =values[3] ** 2
# value5 =values[4] ** 2
# total = value1+value2+value3+value4

# total += g*g
# print ("Sum of Squares" total)
UserIn = input("Enter a comma separated list of numbers :")
values = UserIn.split(",")
total = 0.0
for i in range(len(values)):
    g = float(values[i])
    total += g*g
print("The sum of the square:"+str(total))