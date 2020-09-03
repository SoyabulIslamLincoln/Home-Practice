Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.shape("turtle")
>>> turtle.speed(1)
>>> for i in range(20):
	turtle.forward(10)
	turtle.penup()
	turtle.forward(2)
	turtle.pendown()

	
>>> turtle.exitonclick()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    turtle.exitonclick()
  File "<string>", line 5, in exitonclick
turtle.Terminator
>>> 
