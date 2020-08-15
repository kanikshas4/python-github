#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:46:18 2020

@author: kanikshasharma
"""


def display(name,course= "btec a.i"):
    print("name",name)
    print("course",course)
display(name="reema",course="bca")
display(name="teena")
#%%
var="good"
def display():
    global var
    var="morning"
    print("inside the function: ",var)
display()
print("outside the function: ",var)
var="have a nice day"
print("outside the function: ",var)
#%%
sum = lambda x,y: x+y
print("sum= ",sum(3,5))
#%%
def small(a,b):
    if(a>b):
        return a
    else:
        return b
sum=lambda x,y:x+y
diff=lambda x,y:x-y
print("smallest of the two= ",small(sum(3,2),diff(1,-2)))
#%%
def increment(y):
    return(lambda x:x+1)(y)
a=100
print(a)
b=increment(a)
print(b)
#%%
twice=lambda x:x*2
print(twice(9))

#%%
def myfunc():
    """demonstrate the function"""
    return None
 
