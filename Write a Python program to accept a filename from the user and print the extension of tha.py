Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> file=input("Enter a file name : ")
Enter a file name : lincoln.cpy
>>> extension=filename.split()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    extension=filename.split()
NameError: name 'filename' is not defined
>>> extension=filename.split(".")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    extension=filename.split(".")
NameError: name 'filename' is not defined
>>> extension=file.split(".")
>>> print("the extension of the file is : "+repr(extension[-1]))
the extension of the file is : 'cpy'
>>> 
