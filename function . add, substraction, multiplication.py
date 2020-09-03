Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def ad_number(numbers):
	result=0
	for number in numbers:
		result+=number
	return result

>>> result=ad_number([1,3,5,6,4,6])
>>> print(result)
25
>>> //noew subtraction
SyntaxError: invalid syntax
>>> /subtraction
SyntaxError: invalid syntax
>>> %subtraction
SyntaxError: invalid syntax
>>> def sub_number(numbers):
	result=0
	for number in numbers:
		result-=number
	return result

>>> result=sub_number([2,45,12,45,6])
>>> print(result)
-110
>>> 
>>> 
>>> def mul_number(numbers):
	result=1
	for number in numbers:
		result*=number
	return result

>>> result=mul_number([1,2,3,4,5,6])
>>> print(result)
720
>>> 
