Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.shape("snake")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    turtle.shape("snake")
  File "<string>", line 8, in shape
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named snake
>>> turtle.shape("turtle")
>>> turtle.color("green")
>>> turtle.speed(5)
>>> counter=1
>>> while counter<=120:
	for i in range(2):
		turtle.forward(200)
		turtle.right(90)
	turtle.right(5)
	counter+=1

	
>>> turtle.exitonclick()
>>> 
