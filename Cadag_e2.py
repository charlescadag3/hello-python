

UserIn = int(input("Please type the number of sustained wind in km/h:."))


if UserIn>=220:
 print ("Super Typhoon")
elif UserIn>=118 and UserIn <=220:
 print ("Typhoon")
elif UserIn>=89 and UserIn<=117:
 print ("Severe Tropical Storm")
elif UserIn>=62 and UserIn<=88:
 print ("Tropical Storm")
elif  UserIn>=0 and UserIn<=61: 
 print ("Severe Tropical Storm")
 

