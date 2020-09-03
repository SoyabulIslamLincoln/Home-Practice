Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.random()
0.41510858023537256
>>> random.randint(20,100)
87
>>> random.ranfloat(30.6-100)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    random.ranfloat(30.6-100)
AttributeError: module 'random' has no attribute 'ranfloat'
>>> import turtle
>>> turtle.color("red")
>>> turtle.position()
(0.00,0.00)
>>> turtle.forward(100)
>>> turtle.position()
(100.00,0.00)
>>> turtle.right(90)
>>> turtle.position()
(100.00,0.00)
>>> turtle.forward(200)
>>> 
