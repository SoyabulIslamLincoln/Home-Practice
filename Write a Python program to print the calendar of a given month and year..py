Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import calendar
>>> y=int(input("input the year: "))
input the year: 2019
>>> m=int(input("input the month: "))
input the month: 5
>>> d=int(input("input the day : "))
input the day : 18
>>> print(calender.month(y,m,d))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(calender.month(y,m,d))
NameError: name 'calender' is not defined
>>> print(calendar.month(y,m,d))
                                                              May 2019
      Monday            Tuesday           Wednesday           Thursday            Friday            Saturday            Sunday
                                               1                  2                  3                  4                  5
         6                  7                  8                  9                 10                 11                 12
        13                 14                 15                 16                 17                 18                 19
        20                 21                 22                 23                 24                 25                 26
        27                 28                 29                 30                 31

>>> print(calendar.month(y,m))
      May 2019
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

>>> 
