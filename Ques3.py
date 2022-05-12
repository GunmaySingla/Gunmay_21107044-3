import math
from multiprocessing.connection import answer_challenge
from unittest import result
#Part a
print((3+4)*5)

#Part b
n = int(input("Enter Number-:"))
answer_b = (n*(n-1))/2
print(answer_b)

#Part c
r = int(input("Enter Number-:"))
m = 4*math.pi*(r**2)        
print(m)

#Part d
r_1 = int(input("Enter Number-:"))
a = int(input("Enter Angle in Radians-:"))
b = math.cos(a)
c = math.sin(a)
answer_d = (r_1*(b)*2 + r_1(c)*2)*(1/2)
print('answer_d')

#Part e
y1 = int(input("Enter Number y1"))
y2 = int(input("Enter Number y2"))
x1 = int(input("Enter Number x1"))
x2 = int(input("Enter Number x2"))
answer_e = (y1 - y2)/(x1 - x2)
print('answer_e')




