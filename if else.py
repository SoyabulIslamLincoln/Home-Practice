Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> amount=int(input("enter amount: "))
enter amount: 56
>>> if amount<1000:
	discount=amount*0.05
	print("discount=",discount)

	
discount= 2.8000000000000003
>>> else:
	
SyntaxError: invalid syntax
>>> if amount<1000:
	discount=amount*0.05
	print("discount :",discount)
else:
	discount=amount*0.10
	print("discount:",discount)

	
discount : 2.8000000000000003
>>> print("Net payable= ",amount-discount)
Net payable=  53.2
>>> 
>>> 
>>> fruit=["mango","banana","orange"]
>>> fruit.insert(0,"apple")
>>> fruit.insert(4,"coconut")
>>> fruit
['apple', 'mango', 'banana', 'orange', 'coconut']
>>> item=
SyntaxError: invalid syntax
>>> item="pineapple"
>>> if item in fruit:
	remove(item)
else:
	print(item,"is not in the list")

	
pineapple is not in the list
>>> 
