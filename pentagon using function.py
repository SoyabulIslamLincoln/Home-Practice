Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.shape("turtle")
>>> def triangle(length):
	for i in range(3):
		turtle.forward(length)
		turtle.left(60)

		
>>> counter=0
>>> while counter <4:
	triangle(200)
	counter =counter+1

	
>>> 
