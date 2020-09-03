Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Write a Python program to test whether a number is within 100 of 1000 or 2000
>>> x=int(input("Enter a value: "))
Enter a value: 6546
>>> if x<=100:
	print("the number is within 100")
elif x>100 and x<=1000:
	print("the number is within 1000")
elif x>1000 and x<=2000:
	print("tyhe number is within 2000")
else:
	print("the number is greater than 2000")

	
the number is greater than 2000
>>> 
