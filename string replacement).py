Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> country="North korea"
>>> ncountry=country.replace("North","South")
>>> print(country)
North korea
>>> print(ncountry)
South korea
>>> text="i am doing python"
>>> new_text=text.replace("i","I","python","PyTHon")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    new_text=text.replace("i","I","python","PyTHon")
TypeError: replace() takes at most 3 arguments (4 given)
>>> new_text=text.replace("i","I")
>>> print(text)
i am doing python
>>> print(new_text)
I am doIng python
>>> 
