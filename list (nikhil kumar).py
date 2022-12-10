#!/usr/bin/env python
# coding: utf-8

# In[18]:


def sum_list(a):
    b=0
    c=1
    for i in a:
        
        b=b+i
        c=c*i
    print(b)
    print(c)
sum_list([1,2,3,4,5])


# #### 2. Write a Python function that takes two lists and returns True if they have at least one common
# member.
# Example:
# [1,2,3,4,5], [5,6,7,8,9] = True
# [1,2,3,4,5], [6,7,8,9] = None 
# 

# In[58]:


def nikhil(a,b):
    for i in a:
        for j in b:
            if i==j:
                return  True
            else:
                pass
    print('none')
#nikhil([1,2,3,4,5],[5,6,7,8,9])
nikhil([1,2,3,4,5],[6,6,7,8,9])


# #### 3. Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# + Expected Output:
# + Color1-Color2: ['white', 'orange', 'red']
# + Color2-Color1: ['black', 'yellow']

# In[62]:


a=["red", "orange", "green", "blue", "white"]
b=["black", "yellow", "green", "blue"]
c=set(a)-set(b)
d=set(b)-set(a)
c=list(c)
d=list(d)
print(c)
print(d)


# In[74]:


a=["red", "orange", "green", "blue", "white"]
b=["black", "yellow", "green", "blue"]
c=[]
d=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)  
for i in b:
    if i not in a:
        d.append(i)
print(d)        
        


# In[ ]:





# In[ ]:




