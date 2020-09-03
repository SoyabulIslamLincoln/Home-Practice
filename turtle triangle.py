Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.shape("turtle")
>>> turtle.forward(100)
>>> turtle.left(60)
>>> turtle.left(60)
>>> turtle.forward(100)
>>> turtle.left(120)
>>> turtle.forward(100)
>>> turtle.endonclick()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    turtle.endonclick()
AttributeError: module 'turtle' has no attribute 'endonclick'
>>> turtle.exitonclick()
>>> 
