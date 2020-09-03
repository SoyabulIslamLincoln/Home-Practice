Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=[3,5,7,23]
>>> printlist)
SyntaxError: invalid syntax
>>> print(list)
[3, 5, 7, 23]
>>> list=["3","5","7","23"]
>>> print(list)
['3', '5', '7', '23']
>>> tuple=tpl(list)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple=tpl(list)
NameError: name 'tpl' is not defined
>>> tuple=tuple(list)
>>> print(tuple)
('3', '5', '7', '23')
>>> 
