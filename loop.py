Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> saarc="bangladesh","nepal","bhutan", "india", "srilanka", "pakistan","afganistan"
>>> print(saarc)
('bangladesh', 'nepal', 'bhutan', 'india', 'srilanka', 'pakistan', 'afganistan')
>>> country=input("Entry a country name: ")
Entry a country name: nepal
>>> if country in saarc:
	print(country, "is a memeber of SAARC")
	print("program terminated")

nepal is a memeber of SAARC
program terminated
>>> saarc.py
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    saarc.py
AttributeError: 'tuple' object has no attribute 'py'
>>> country=inuput("Enter a country name :")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    country=inuput("Enter a country name :")
NameError: name 'inuput' is not defined
>>> 
