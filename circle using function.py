Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.shape("turtle")
>>> turtle.color("red")
>>> def square(side_length):
	for i in range(4):
		turtle.forward(side_length)
		turtle.left(90)

		
>>> counter=0
>>> while counter <90:
	square(100)
	turtle.right(4)
	counter=counter +1

	
>>> turtle.exitonclick()
>>> 
