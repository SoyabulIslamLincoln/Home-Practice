Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editorexam_st_date = (11, 12, 2014)Sample Output : The examination will start from : 11 / 12 / 2014
>>> exam_date=(11,12,2019)
>>> exam=str(exam_date)
>>> exam
'(11, 12, 2019)'
>>> data=exam.split(",")
>>> data
['(11', ' 12', ' 2019)']
>>> #bal hoilo na to
>>> exam_date=(11,12,2014)
>>> print("The time of tyhe exam is : %i / %i / %i "%exam_date)
The time of tyhe exam is : 11 / 12 / 2014 
>>> #akhon hoise bal
>>> 
