Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> now=datetime.datetime.now()
>>> print("curent date time: ")
curent date time: 
>>> print(now.strftime("%Y - %m - %d  %H:%M :%S)
		       
SyntaxError: EOL while scanning string literal
>>> print(now.strftime("%Y - %m - %d  %H:%M :%S))
		       
SyntaxError: EOL while scanning string literal
>>> print(now.strftime("%Y - %m - %d  %H:%M :%S"))
		       
2019 - 05 - 17  22:32 :09
>>> 
