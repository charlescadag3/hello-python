

UserIn = float(input("Please type the number of sustained wind in km/h:"))


if UserIn>=220.0:
 print ("Super Typhoon")
elif UserIn>=118.0 and UserIn <=220.0:
 print ("Typhoon")
elif UserIn>=89.0 and UserIn<=117.0:
 print ("Severe Tropical Storm")
elif UserIn>=62.0 and UserIn<=88.0:
 print ("Tropical Storm")
elif  UserIn>=1. and UserIn<=61.0: 
 print ("Tropical Depression")
 

