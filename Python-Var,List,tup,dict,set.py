Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 9-4
5
>>> 4*6
24
>>> 8/4
2.0
>>> 5/2
2.5
>>> 8+9-
SyntaxError: invalid syntax
>>> 8+4
12
>>> 'sai'
'sai'
>>> ' sai is a good boy's'
SyntaxError: invalid syntax
>>> 'sai is a good boy\'s'
"sai is a good boy's"
>>> 2*sai
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    2*sai
NameError: name 'sai' is not defined
>>> 2*'sai'
'saisai'
>>> print('c:\doc\py\nzen')
c:\doc\py
zen
>>> print(r'c:\doc\py\nzen')
c:\doc\py\nzen
>>> 
>>> x=2
>>> x+3
5
>>> y=2
>>> x+y
4
>>> x+10
12
>>> x=5
>>> x+1
6
>>> x+y
7
>>> name='saikiran'
>>> name+chinthaginjala
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name+chinthaginjala
NameError: name 'chinthaginjala' is not defined
>>> name +'\ chinthaginjala'
'saikiran\\ chinthaginjala'
>>> name+'chintha'
'saikiranchintha'
>>> name+' chinthaginjala
SyntaxError: EOL while scanning string literal
>>> name+' chinthaginjala'
'saikiran chinthaginjala'
>>> name = 'youtube'
>>> name[-1]
'e'
>>> name[-2]
'b'
>>> name[0:2]
'yo'
>>> name[1:5]
'outu'
>>> name[1:]
'outube'
>>> name[:]
'youtube'
>>> name[:5]
'youtu'
>>> name[4:13]
'ube'
>>> name[0:2]='my'
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    name[0:2]='my'
TypeError: 'str' object does not support item assignment
>>> name = 'youtube'
>>> name[3:1]='sa'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    name[3:1]='sa'
TypeError: 'str' object does not support item assignment
>>> 'my '+name[3:]
'my tube'
>>> name
'youtube'
>>> myname= 'Sai Kiran Chinthaginjala'
>>> len(myname)
24
>>> number = [30,40,44,33]
>>> number
[30, 40, 44, 33]
>>> number[]
SyntaxError: invalid syntax
>>> number[:]
[30, 40, 44, 33]
>>> number[3]
33
>>> number[-3:]
[40, 44, 33]
>>> number[-2]
44
>>> number[-3]
40
>>> number[-1]
33
>>> names =['s','k','z']
>>> names
['s', 'k', 'z']
>>> val = [9.5,'s',25]
>>> mul=[names,number]
>>> mul
[['s', 'k', 'z'], [30, 40, 44, 33]]
>>> number = [-3:-1]
SyntaxError: invalid syntax
>>> number = [-3:1]
SyntaxError: invalid syntax
>>> number = [-3:]
SyntaxError: invalid syntax
>>> num=[20,10,11,24,13,244]
>>> num=[-3:-1]
SyntaxError: invalid syntax
>>> num[-3:1]
[]
>>> num[-3:-1]
[24, 13]
>>> num[-3:0]
[]
>>> num[-3:-2]
[24]
>>> num[-3:-1]
[24, 13]
>>> num[-2:1]
[]
>>> num[-1:-5]
[]
>>> num
[20, 10, 11, 24, 13, 244]
>>> nums.append('s')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    nums.append('s')
NameError: name 'nums' is not defined
>>> num.append('s')
>>> num
[20, 10, 11, 24, 13, 244, 's']
>>> num.sort()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    num.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> num.clear()
>>> num
[]
>>> num=[10,20,30,40,50,60,70]
>>> num.append(1,2)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    num.append(1,2)
TypeError: list.append() takes exactly one argument (2 given)
>>> num.insert(1,2)
>>> num
[10, 2, 20, 30, 40, 50, 60, 70]
>>> num.sort()
>>> num
[2, 10, 20, 30, 40, 50, 60, 70]
>>> num.remove(2)
>>> num.pop(1)
20
>>> num
[10, 30, 40, 50, 60, 70]
>>> number=[20,40,50,70,80]
>>> number.append(10)
>>> number
[20, 40, 50, 70, 80, 10]
>>> number.insert(1,100)
>>> number
[20, 100, 40, 50, 70, 80, 10]
>>> number.remove(100)
>>> number
[20, 40, 50, 70, 80, 10]
>>>  number.pop(1)
 
SyntaxError: unexpected indent
>>> number.pop(1)
40
>>> number.pop()
10
>>>  number.extend([39,339])
 
SyntaxError: unexpected indent
>>> number.extend([39,339])
>>> number
[20, 50, 70, 80, 39, 339]
>>> min(number)
20
>>> max(number)
339
>>> sum(number)
598
>>> t=(10,20,30,40,50,60,70)
>>> t=[1]
>>> t
[1]
>>> t[1]
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    t[1]
IndexError: list index out of range
>>> t=(10,20,30,40,50,60,70)
>>> t[1]
20
>>> t[1]=5
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    t[1]=5
TypeError: 'tuple' object does not support item assignment
>>> t.count()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> t.count(1)
0
>>> t
(10, 20, 30, 40, 50, 60, 70)
>>> t.append(11)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    t.append(11)
AttributeError: 'tuple' object has no attribute 'append'
>>> z=list[t]
>>> z
list[10, 20, 30, 40, 50, 60, 70]
>>> z=list(t)
>>> z
[10, 20, 30, 40, 50, 60, 70]
>>> z.append[1000,2000]
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    z.append[1000,2000]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> z.append(1000,2000)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    z.append(1000,2000)
TypeError: list.append() takes exactly one argument (2 given)
>>> z.append(1)
>>> z
[10, 20, 30, 40, 50, 60, 70, 1]
>>> z.append(1000)
>>> t=tuple(z)
>>> t
(10, 20, 30, 40, 50, 60, 70, 1, 1000)
>>> s={10,15,20,25,30}
>>> s
{20, 25, 10, 30, 15}
>>> s.add(100)
>>> s
{20, 100, 25, 10, 30, 15}
>>> s.add(5000,200)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    s.add(5000,200)
TypeError: set.add() takes exactly one argument (2 given)
>>> dat={1:'Name',2:'kiran',3:'sai',4:'sub'}
>>> dat
{1: 'Name', 2: 'kiran', 3: 'sai', 4: 'sub'}
>>> dat[2]
'kiran'
>>> dat[4]
'sub'
>>> dat.get(2)
'kiran'
>>> dat.get(100:'not ound')
SyntaxError: invalid syntax
>>> dat.get(100,'not found')
'not found'
>>> dat
{1: 'Name', 2: 'kiran', 3: 'sai', 4: 'sub'}
>>> keys=['sai','kiran','tony','rama']
>>> values=['python','ds','da','java']
>>> data= dict(zip(keys,values))
>>> data
{'sai': 'python', 'kiran': 'ds', 'tony': 'da', 'rama': 'java'}
>>> data.get('sai')
'python'
>>> data['monika']='compu'
>>> data
{'sai': 'python', 'kiran': 'ds', 'tony': 'da', 'rama': 'java', 'monika': 'compu'}
>>> del data['rama']
>>> data
{'sai': 'python', 'kiran': 'ds', 'tony': 'da', 'monika': 'compu'}
>>> prog={'sai':'python','kiran':['DA','DS','CSE'],'Bala':{'sect1':'DL','Sect2:'NLP','sect3':'Bigdata'}}
						       
SyntaxError: invalid syntax
>>> prog={'sai':'python','kiran':['DA','DS','CSE'],'Bala':{'sect1':'DL','Sect2':'NLP','sect3':'Bigdata'}}
>>> prog['sai']
'python'
>>> prog['Bala']['sect1']
'DL'
>>> 