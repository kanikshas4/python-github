#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:48:24 2020

@author: kanikshasharma
"""


#%%
def cube():
    n=int(input("enter the number: "))
    print("the number is: ",n)
    c=n*n*n
    print("cube of the number is: ",c)
cube() 
#%%
def cube(n):
    print("the number is ",n)
    c=n*n*n
    print("the cube of the number is: ",c)
cube(5)
#%%
def circlearea():
    r=int(input("enter the radius of circle"))
    PI=3.14
    area=1
    area=PI*r*r
    print("the area of the circle",area)
circlearea()
#%%
def circlearea(rad):
    print("the radius of the circle",rad)
    PI=3.14
    area=1
    area=rad*rad*PI
    print("the area of the circle: ",area)
circlearea(5)
#%%
def sum():
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    if n1>n2:
        n2=n2,n1
    sum=0
    for i in range(n1,n2+1,1):
        sum=sum+1
        print(i)
    print("sum of all numbers in between",n1,"to",n2,"is",sum)
sum()
#%%
def sum(n1,n2):
    if n1>n2:
        n2=n2,n1
    sum=0
    for i in range(n1,n2+1,1):
        sum=sum+1
        print(i)
    print("sum of all the numbers in between",n1,"to",n2,"is",sum)
sum(2,7)
#%%
def sum(n1,n2):
    if n1>n2:
        n2=n2,n1
    sum=0
    for i in range(n1,n2+1,1):
        sum=sum+1
        print(i)
    print("sum of all the numbers in between",n1,"to",n2,"is",sum)
sum(n2=9,n1=2)
#%%
def func(let1,let2):
    let=let1+let2
    print("the concatenated let",let)
let1=str(input("enter the 1st let: "))
let2=str(input("enter the 2nd let: "))
func(let1,let2)
#%%
def func(let1,let2):
    let=let1+let2
    print("the charecter: ",let)
let1=str(input("enter 1st charecter: "))
let2=str(input("enter 2nd charecter: "))
func(let2,let1)
#%%
def func(let1,let2="world"):
    let=let1+let2
    print("the charecter: ",let)
func(let1="hello",let2="everyone")
func(let1="hey")

