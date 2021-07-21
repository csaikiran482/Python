Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=5
>>> id(num)
2722668571056
>>> name='sai'
>>> id(name)
2722711637936
>>> a=10
>>> b=a
>>> id(a)
2722668571216
>>> id(b)
2722668571216
>>> k=10
>>> id(k)
2722668571216
>>> pi=2.14
>>> type(pi)
<class 'float'>
>>> num=2.5
>>> type(num)
<class 'float'>
>>> num=5
>>> type(num)
<class 'int'>
>>> num=6+9j
>>> type(num)
<class 'complex'>
>>> k=5.6
>>> a=int(k)
>>> a
5
>>> b=10
>>> c=float(b)
>>> c
10.0
>>> type(c)
<class 'float'>
>>> c=complex(b,c)
>>> c
(10+10j)
>>>  b<c
 
SyntaxError: unexpected indent
>>> b<c
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b<c
TypeError: '<' not supported between instances of 'int' and 'complex'
>>> b
10
>>> c
(10+10j)
>>> a
5
>>> b
10
>>> a<b
True
>>> a>b
False
>>> list=[25,35,45]
>>> type(list)
<class 'list'>
>>> s={2,2,,,3,3,}
SyntaxError: invalid syntax
>>> s={3,4,5,6,7}
>>> type(s)
<class 'set'>
>>> t=(25,45,35)
>>> type(t)
<class 'tuple'>
>>> str='sai'
>>> type(str)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
>>> list(range(10))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
>>> range(10)
range(0, 10)
>>> list(range(10))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
>>> a=list(range(10))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a=list(range(10))
TypeError: 'list' object is not callable
>>> list[range(2,10,2)]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    list[range(2,10,2)]
TypeError: list indices must be integers or slices, not range
>>> list(range(2,10,2))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    list(range(2,10,2))
TypeError: 'list' object is not callable
>>> 
>>> range(10)
range(0, 10)
>>> type(range(10))
<class 'range'>
>>> list(range(10))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
>>> d={'S':'Sai','A':'Apple','B':'Boy'}
>>> d.keys()
dict_keys(['S', 'A', 'B'])
>>> d.values()
dict_values(['Sai', 'Apple', 'Boy'])
>>> d['Apple']
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    d['Apple']
KeyError: 'Apple'
>>> d['A']
'Apple'
>>> x=x+2
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    x=x+2
NameError: name 'x' is not defined
>>> x=2
>>> x=X+2
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    x=X+2
NameError: name 'X' is not defined
>>> x=x+2
>>> x
4
>>> x+=2
>>> x
6
>>> x*=3
>>> x
18
>>> a=6
>>> b=7
>>> a==b
False
>>> c=7
>>> b==c
True
>>> b>=c
True
>>> b>c
False
>>> b!=c
False
>>> a!=c
True
>>> clc
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    clc
NameError: name 'clc' is not defined
>>> 
>>> 
>>> 
>>> 

>>> 


>>> 

>>> 

>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 
>>> a=5,b=4
SyntaxError: cannot assign to literal
>>> a=5:b=4
SyntaxError: invalid syntax
>>> a=4;b=5
>>> a<8 and b<10
True
>>> a<2 and b>2
False
>>> a<2 and b<2
False
>>> a=5
>>> b=6
>>> temp =a
>>> a=b
>>> b=temp
>>> print(a)
6
>>> print(b)
5
>>> a=5
>>> b=6
>>> a,b=b,a
>>> a;b
6
5
>>> ~12
-13
>>> ~5
-6
>>> ~7
-8
>>> 12 &13
12
>>> 12|13
13
>>> 25&30
24
>>> 12^13
1
>>> 10<<2
40
>>> 10>>2
2
>>> import math
>>> x=math.sqrt
>>> x=math.sqrt(100)
>>> x
10.0
>>> print(math.sqrt(100))
10.0
>>> print(math.sqrt(25))
5.0
>>> print(math.pow(100,2))
10000.0
>>> print(math.pi)
3.141592653589793
>>> print(math.floor(2.934))
2
>>> print(math.ceil(2.934))
3
>>> print(math.ceil(2.4999))
3
>>> print(math.floor(2.999))
2
>>> from math import sqrt,pow
>>> pow(4,5)
1024.0
>>> 