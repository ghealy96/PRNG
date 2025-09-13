import math
end="\n"


#PART 1.1A:
name = "Griffin"
age = 29
height = 5.83
favorite_color = "green"
#PART 1.2A&B:
print(name)
print(age)
print(height)
print(favorite_color)
print(name,age,height,favorite_color)
#PART: 1.2C
print(end)
print(f"hello: my {name} is and im {age} years old")
print(f"hello: my {name} is and im {age:f} years old")
print(f"hello: my {name} is and im {age:d} years old")
print(f"hello: my {name} is and im {age:.2f} years old")
#PART: 1.2D
print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
the end""")
print("")
#PART 2
rad=5
circle_area = math.pi*rad**2
print(f"Circle Area: {circle_area:.1f}")

print("square root of my age is", round(math.sqrt(age),2))
print("sin of my height is", round(math.sin(height),2),)
print("cos of my height is", round(math.cos(height),2),end)



#PART 3
print((age+5))
print((height-4))
print((age*height))
print(height/2)
print((age%3))
print((age**2))

#PART 4

def temp_converter(temp , degrees):

 if degrees.upper()== "F":
       return ((temp - 32) * 5 / 9)
 elif degrees.upper() == "C":
        return((temp * 5 / 9) + 32)
 else:
    return(temp)


temp=int(input("enter temperature as a whole number:"))
degrees=input("is this in Celsius or Fahrenheit? type c or f:")
print("it is",temp_converter(temp, degrees),'\u00b0', "F" if degrees == "C" else "C")