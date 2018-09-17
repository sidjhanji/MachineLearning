#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:07:28 2018

@author: sjhanji
"""

# Python for Datascience

def foo(x):
    print(x)
    print(x*2)
    
foo(2)


str = 'siddharth'
for letter in str:
    print(letter)
    
str1 = 'sid'
str2 = 'jhanji'
print (str1 +' '+ str2)   

lst = ['Apples', 'Oranges', 'Blueberrries', 2017]
lst[0]
lst[3]
len(lst)

lst[:2]
lst[1]='sid'
lst

lst.append('siddharth')
lst

'sid' in lst

'siddie' in lst

lst2 = ['chocolate','bite']
lst3 = lst + lst2

lst3

len(lst3)


counts = dict()
names = ['sid','rahul', 'vaibhav', 'sid', 'rahul','sid','sid']
for name in names:
    counts[name] = counts.get(name, 0) + 1
counts
print(counts.items())
print(sorted(counts.items(), key=lambda x: x[1]))
print(sorted(counts.items(), key=lambda x: x[1]))






print(sorted(counts.items(), key=lambda x: x[1]))


print(sorted(counts.items(), key=lambda x: x[1]))


print(sorted(counts.items(), key=lambda x: x[1], reverse=True))


tup = ()

tup1 = ('sid', 1, 'jhanji', 2)
tup1

tup1[:2]

(x, y, z) = ('sid', 'jhanji', 2)
x
y
z

str = 'Siddharth Jhanji'
for letter in str:
    print(letter)
    
lst = ['Sid', 'Jhanji', 'is', 'doing', 'good']
for item in lst:
    print(item)
    
    
    
dct = {"Key": "value", "Summer": "Hot", "Winter": "Cold"}
for key, value in dct.items():
    print(key, value)
    

    