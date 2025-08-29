import math


Radius1 = 5
Area1=math.pi*(Radius1**2)
Area2=4/3*math.pi*(3**3)
print("Area of circle with radius of 5 is ")
print(Area1)
print("Area of sphere with radius of 3 is ", Area2)
print("hypotenuse of right triangle with side 3 & 4 = " , math.sqrt((3**2) + (4**2)) )


FirstName="Griffin"
LastName="Healy"
NameTag=FirstName+" "+LastName
NameTag.upper()
NameTag=NameTag.lower()
print(NameTag," has ", len(NameTag.replace(" ","")), " characters in his name ", NameTag)


Age = 29
Height = 5.83
Weight = 172
print("age data type is ", type(Age))
print("Height data type is ", type(Height))
print("Weight data type is ", type(Weight))
print("my bmi is ",round( Weight/ ( round(Height*12) **2 ) *703,1 ) )
