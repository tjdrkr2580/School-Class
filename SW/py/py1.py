from re import X


t = ()
xy = (2560,1440)
color= 129,247,216
print(xy + color)
print(xy * 2)

color = 129,247,216
red , green , blue = color
print(red)
print(green)
print(blue)
type(red)

x = 2560
y = 1440
x , y = y , x
print(x)
print(y)


a = (123,"abc",True,123)
print(a[1])
print(a[2:])
print(a[:2])

s3 = {3,6,9,12}
s4 = {4,8,12,16}
print(s3 & s4) 

a = True
b = False
print(type(a))