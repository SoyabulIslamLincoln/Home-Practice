Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.shape("turtle")
>>> height=5
>>> width=5
>>> turtle.speed(1)
>>> turtle.penup()
>>> for y in range (height):
	forx in range (width):
		turtle.dot()
		turtle.forward(20)
		
SyntaxError: invalid syntax
>>> for y in range (height):
	for x in range(width):
		turtle.dot()
		turtle.forward(20)
	turtle.backward(20*width)
	turtle.right(90)
	turtle.forward(20)
	turtle.left(90)

	
>>> turtle.exitonclick()
>>> 
