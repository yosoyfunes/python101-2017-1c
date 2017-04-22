>>> class Auto(object):
...     def __init__(self):
...         pass
...     def __add__(self, other):
...         return 2
...
>>> Auto() + Auto()
2
