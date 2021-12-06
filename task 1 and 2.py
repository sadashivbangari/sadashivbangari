#!/usr/bin/env python
# coding: utf-8

# In[3]:


#  task 1. go through some built in functions

#1. abs()
a=abs(-5.6)
print(a)


# In[4]:


#2. type()
b=type("Hii")
print(b)


# In[6]:


#3. round()
value=round(55.6789)
print(value)


# In[12]:


#4. set()
l1=(11,45.3,"messi","ronaldo")
print("l1[2:3]=",l1[2:3])


# In[20]:


#5 character()
value=chr(97)
print(value)


# In[36]:


#6 sorted()
value=(25,1,675,88,-90)
l3=sorted(value)
print(l3)


# In[48]:


#7 all()
value = [11, 12, 13, 14, 15]
print(all(value))


# In[65]:


#8 eval()
a=2
b=3
print(eval('a+b+2*a*b'))


# In[66]:


#9 pow()
d=pow(6,4)
print(d)


# In[67]:


#10 bin()
num =120
print(bin(num))


# In[1]:


#11 expandtabs()
txt = "w\te\tl\tc\to\tm\te"
a=txt.expandtabs(2)
print(a)


# In[13]:


#12 index()
txt ="messi won the copa america"
b=txt. index("copa")
print(b)


# In[24]:


#13 join()
C=("messi",'neymar',"suarez")
d="".join(C)
print(d)


# In[27]:


#14 replace()
E= "i love to play basketball"
d=E.replace("basketball","football")
print(d)


# In[28]:


#15 rindex()
f="very pretty lady"
F=f.rindex("lady")
print(F)


# In[30]:


# 16 split()
g="its very dark night"
G=g.split()
print(G)


# In[31]:


#17 zfill()
h="hii"
H=h.zfill(5)
print(H)


# In[33]:


#18 append()
I=['cycle','bike']
I.append('car')
print(I)


# In[34]:


#19 fromkeys()
a=('s','p','q')
b=(1,2,3)
c=dict.fromkeys(a,b)
print(c)


# In[35]:


#20 update()
fifa ={
    "2018":"year",
    "winner":"france"
}
fifa.update({"bestplayer":"modric"})
print(fifa)


# In[36]:


#21 discard()
f={1,2,3,4,5,6}
f.discard(5)
print(f)


# In[55]:


# task 2 : given string check 'to' is present 
# string="welcome to python"
string="welcome to python"
"to" in string


# In[ ]:





# In[ ]:




