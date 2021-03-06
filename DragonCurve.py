"""
Dragon Curve Visualiser
Created by Gainsboroow 
Github : https://github.com/Gainsboroow
Github Repository : https://github.com/Gainsboroow/Dragon-Curve

How to use : 
Enter the number of folds you want. Look at the results !
"""

from turtle import *
from copy import deepcopy


nbFolds = int(input("How many folds : "))

wn = Screen()
wn.bgcolor("black")

hideturtle()
pencolor("red")
a = []
speed(0)

for z in range(nbFolds):
    copie = deepcopy(a)
    for i in copie[::-1]:
        a.append(1-i)
    a.insert(len(a)//2, 0)

down()
length = 20
forward(length)
for i in a:
    if i:
        right(90)
    else:
        left(90)
    forward(length)

exitonclick()
