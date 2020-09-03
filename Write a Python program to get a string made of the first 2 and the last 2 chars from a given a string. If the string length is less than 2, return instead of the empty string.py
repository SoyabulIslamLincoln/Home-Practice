Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def string(str):
	if len(str)<2:
		return("empty string")
	return str[0:2] + str[-2:]

>>> print(string("westros"))
weos
>>> print(string("wes"))
wees
>>> print(string("we"))
wewe
>>> print(string("w"))
empty string
>>> 
