#!/usr/bin/env python
# coding: utf-8

# In[1]:


#using while loop print no's from 10 to 1
a=10
while(a>0):
    print(a)
    a=a-1


# In[3]:


#for loop to loop over tuples,sets and dictionary
#tuple
tuple=("car","bike","tractor","truck")
for a in tuple:
    print(a)

#sets
set={"leo","rooney","7","fifa"}
for b in set:
    print(b)

#dictionary
dict={"messi":7,"ronaldo":5}
for c in dict:
    print(c)
    


# In[5]:


# what is the usage of continue with the example
"""the continue statement instucts a loop to continue to the next iteration"""
#for while loop
i=0
while i<12:
    i+=1
    if i==5:
        continue
    print(i)

#for loop
for i in range(5):
    i+=1
    if i==2:
        continue
    print(i)


# In[6]:


#pass keyword with example
"""pass keyword is used to execute nothing: it means, when we don't want to execute code, the pass can be used to execute empty"""
class person:
    pass


# In[ ]:




