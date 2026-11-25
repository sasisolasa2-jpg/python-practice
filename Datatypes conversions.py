Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes conversions
#nt
int(5)
5
int(6.5)
6
int("hello")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
int(8+5j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(8+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
float(8)
8.0
float(8.5)
8.5
float("nellore")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float("nellore")
ValueError: could not convert string to float: 'nellore'
>>> float(5+7j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(5+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> str(6)
'6'
>>> str(8.7)
'8.7'
>>> str("tirupati")
'tirupati'
>>> str(6+8j)
'(6+8j)'
>>> str(True)
'True'
>>> complex(2)
(2+0j)
>>> complex(7.8)
(7.8+0j)
>>> complex("tirupati")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    complex("tirupati")
ValueError: complex() arg is a malformed string
>>> complex(8+6j)
(8+6j)
>>> complex(True)
(1+0j)
>>> bool(6)
True
>>> bool(6.8)
True
>>> bool("nellore")
True
>>> bool(6+8j)
True
>>> bool(True)
True
