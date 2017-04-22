class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A()

a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)

a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)

A.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)


'''
Staticmethods are used to group functions which have some logical connection with a class to the class.
'''

'''
With staticmethods, neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class:
'''
a.static_foo(1)
# executing static_foo(1)

A.static_foo('hi')
# executing static_foo(hi)

'''
foo is just a function, but when you call a.foo you don't just get the function, you get a "partially applied" version of the function with the object instance a bound as the first argument to the function. foo expects 2 arguments, while a.foo only expects 1 argument.

a is bound to foo. That is what is meant by the term "bound" below:
'''
print(a.foo)
# <bound method A.foo of <__main__.A object at 0xb7d52f0c>>

'''
With a.class_foo, a is not bound to class_foo, rather the class A is bound to class_foo.
'''

print(a.class_foo)
# <bound method type.class_foo of <class '__main__.A'>>
'''
Here, with a staticmethod, even though it is a method, a.static_foo just returns a good 'ole function with no arguments bound. static_foo expects 1 argument, and a.static_foo expects 1 argument too.
'''
print(a.static_foo)
# <function static_foo at 0xb7d479cc>
'''
And of course the same thing happens when you call static_foo with the class A instead.
'''
print(A.static_foo)
# <function static_foo at 0xb7d479cc>



'''
>>> class DictSubclass(dict):
...     def __repr__(self):
...         return "DictSubclass"
...
>>> dict.fromkeys("abc")
{'a': None, 'c': None, 'b': None}
>>> DictSubclass.fromkeys("abc")
DictSubclass
'''


'''
@staticmethod function is nothing more than a function defined inside a class. It is callable without instantiating the class first. It’s definition is immutable via inheritance.

@classmethod function also callable without instantiating the class, but its definition follows Sub class, not Parent class, via inheritance. That’s because the first argument for @classmethod function must always be cls (class).
'''
