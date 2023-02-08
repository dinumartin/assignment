#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a Python Program to accept the details of a student like name, roll number and mark and display it.
name =(input('Enter the name:'))
rollnumber=int(input('Enter the roll number:'))
mark=int(input('Enter the mark:'))
print('Name:',name,'\nRoll no:',rollnumber,'\nMark:',mark)


# In[1]:


#Write a Python program to convert temperatures to and from Celsius Fahrenheit.
l=input('Type y if your temperature is in celsius:')
t=int(input('Enter the Temperature : '))
l=l.lower()
if (l=='y'):
    f=(t*(9/5)+32)
    print('Temperature in Fahrenheit :',f)
else:
    c=(t-32)*(5/9)
    print('Temperature in celsius :',c)


# In[5]:


#Write a Python program to accept two numbers from the user and display
#its product
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
print('product of the numbers:',a*b)


# In[17]:


#Write a Python program to accept the radius of a circle and display its area.
import math
r=int(input('Enter the radius:'))
A=(math.pi*r*r)
print('Area of the circle:',A)


# In[21]:


#Python program to insert a number to any position in a list
lst = [5,4,7,8,9]
print("list =",lst)
insertitem=int(input('enter the number to insert:'))
indexvalue=int(input('Enter the position:'))
lst.insert(indexvalue,insertitem)
print('new list',lst)


# In[32]:


#7th 
sample_dict = { "name": "John", "age":5, "salary": 8000, "city": "New York"}
print('initial 1st dictionary',sample_dict)
sample_dict.update({"city":"Delhi"})
print(sample_dict)


# In[36]:


#8th
sample_dict = {
'emp1': {'name': 'John', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 500}
}
print(sample_dict)
sample_dict.update({'emp3': {'name': 'Brad', 'salary': 8500},})
print('updated dict:',sample_dict)


# In[5]:


#Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50,83,567,50,81)
import operator as op
print(op.countOf(tuple1,50))


# In[ ]:




