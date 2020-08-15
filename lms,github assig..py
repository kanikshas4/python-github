#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:13:35 2020

@author: kanikshasharma
"""


def GCD(x,y):
    rem=x%y
    if(rem==0):
        return y
    else:
        return GCD(y,rem)
n=int(input("enter the first number: "))
m=int(input("enter the second number: "))
print("the GCD of numbers is: ",GCD(n,m))
#%%
def exp_rec(x,y):
    if(y==0):
        return 1
    else:
        return(x*exp_rec(x,y-1))
n=int(input("enter the 1st number: "))
m=int(input("enter the 2nd number: "))
print("result= ",exp_rec(n,m))
#%%
def fibonnaci(n):
    if(n<2):
        return 1
    else:
        return (fibonnaci(n-1)+fibonnaci(n-2))
n=int(input("enter the number of terms: "))
for i in range(n):
    print("fibbonaci(",i,")=",fibonnaci(i))
#%%
def func(n,count=0):
    if n==0:
        return count
    else:
        return func(n-1,count+1)
print("number of times the function was called is: ",func(100))
#%%
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)
#%%
def small(a,b):
    if(a>b):
        return b
    else:
        return a
sum=lambda x,y:x+y
diff=lambda x,y:x-y
print("smaller of the two number is: ",small(sum(8,7),diff(0,-1)))
#%%
def concatenate(string1,string2):
    string3="empty string"
    if len(string1)>0:
        string1+=string2
        return string1
    else:
        return string3
string1=input("enter 1st string value: ")
string2=input("enter 2nd string value: ")
print("concatenated string: ",concatenate(string1,string2))