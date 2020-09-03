Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True:
	n=input("Please enter a positive number(0 to exit): ")
	n=int(n)
	if n<0:
		print("we only allow positive number.please try again")
		continue
	if n==0:
		break
	print("square of", n "is",n*n)
	
SyntaxError: invalid syntax
>>> while True:
	n=input("enter a positive number(0 to exit):")
	n=int(n)
	if n<0:
		print("Try again")
		continue
	if n==0:
		break
	print("square of",n,"is",n*n)

	
enter a positive number(0 to exit):5
square of 5 is 25
enter a positive number(0 to exit):-8
Try again
enter a positive number(0 to exit):8
square of 8 is 64
enter a positive number(0 to exit):23344
square of 23344 is 544942336
enter a positive number(0 to exit):4
square of 4 is 16
enter a positive number(0 to exit):554654
square of 554654 is 307641059716
enter a positive number(0 to exit):5476576898
square of 5476576898 is 29992894519707302404
enter a positive number(0 to exit):0
>>> 
