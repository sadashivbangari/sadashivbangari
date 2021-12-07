#!/usr/bin/env python
# coding: utf-8

# In[5]:


# other built in functions
# remove()
a=[1,2,3,4,5,6,7]
a.remove(4)
print(a)


# In[9]:


#count()
x=[1,4,9,8,9,'ball','stick',9]
y=x.count(9)
print(y)


# In[16]:


#clear()
m=["ronaldo","messi","neymar"]
m.clear()
print(m)


# In[17]:


#sort()
o=[2,455,67,15,3]
o.sort()
print(o)


# In[23]:


#reverse
p='all of you'[::-1]
print(p)


# In[25]:


# create a list of length=10 and access 5th to 8th data
p=[1,2,3,4,5,6,7,8,9,10]
print(p[5:8])


# In[35]:


#add item 70 after 60 in the following list
l1=[10,20,[30,40,[50,60],80],90,100]
l1[2][2].insert(2,70)
print(l1)


# In[40]:


#add sublist[7,8]after6
l2=[1,2,[3,4,5,6],9]
l2[2].insert(4,[7,8])
print(l2)


# In[ ]:




