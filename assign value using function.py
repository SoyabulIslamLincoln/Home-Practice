Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def myfunc(x):
	print("inside myfunction",x)
	x=10
	print("inside myfunc",x)

	
>>> x=15
>>> myfunc(x)
inside myfunction 15
inside myfunc 10
>>> print(x)
15
>>> def myfuc(y=10):
	print("y=",y)

	
>>> x=20
>>> myfunc(x)
inside myfunction 20
inside myfunc 10
>>> myfuc(x)
y= 20
>>> myfuc()
y= 10
>>> 
