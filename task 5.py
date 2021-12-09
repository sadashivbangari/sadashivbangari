#!/usr/bin/env python
# coding: utf-8

# In[1]:


# do following tasks for given dictionary
dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}
#accessing mike
dict1["april_batch"]["student"]["name"]


# In[2]:


#access 80
dict1["april_batch"]["student"]["marks"]["python"]


# In[4]:


#change name 'mike' to "your name"
dict1= {"april_batch":{"student":{"name":"mike","marks":{"python":80,"marks":70}}}}
dict1["april_batch"]["student"]["name"]="sadashiv"
print(dict1)


# In[5]:


#add ML=80 and DL=80 inside marks
dict1["april_batch"]["student"]["marks"].update({"ML":80,"DL":80})
print(dict1)


# In[ ]:




