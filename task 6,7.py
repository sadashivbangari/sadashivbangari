#!/usr/bin/env python
# coding: utf-8

# In[16]:


#add and remove the element from tuple
tuple1=(1,2,5,6,9,'abhi','sentiment')
#add element.
tuple1=tuple1 + (10,)
print(tuple1)


# In[20]:


#remove element
n=7
tuple1=tuple1[:n]+tuple1[n+1:]
print(tuple1)


# In[21]:


#sets inbuilt method
#difference and symmetric_difference
#1.difference
a={1,2,3,4,5}
b={3,5,7,9}
c=a.difference(b)
print(c)
d=b.difference(a)
print(d)


# In[22]:


#2.symmetric_difference
e=a.symmetric_difference(b)
print(e)


# In[ ]:




