import importlib
import testfunc
print(importlib)
print(importlib.__doc__)
print(testfunc.testfunc())
input("press to cont")
importlib.reload(testfunc)
print(testfunc.testfunc())
print("hello")
