Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n=int(input("Enter a number : "))
Enter a number : 56
>>> n1=int("%s"%n)
>>> n2=int("%s%s"%(n,n))
>>> n3=("%s%s%s"%(n,n,n))
>>> n1
56
>>> n2
5656
>>> n3
'565656'
>>> print(n1+n2+n3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(n1+n2+n3)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> n3=int("%s%s%s"%(n,n,n))
>>> n3
565656
>>> print(n1+n2+n3)
571368
>>> 
