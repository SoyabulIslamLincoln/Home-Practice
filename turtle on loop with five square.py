Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.shape("turtle")
>>> turtle.speed(1)
>>> for sidelength in range(50,100,10)
SyntaxError: invalid syntax
>>> for side_length in range(50,100,10):
	for i in range(4):
		turtle.forward(side_length)
		turtle.left(90)

		
>>> turtle.exitonclick()
>>> 
