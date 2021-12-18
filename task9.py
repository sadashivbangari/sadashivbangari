#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ask 2 numbers from users and store it in num1 and num2
#Ask user to press 1 for addition,2 for subtraction,3 for multiplication and 4 for division
#based on number given by user do the math operation
def switch():
    a=int(input("enter first value:"))
    b=int(input("enter secound value:"))
    print("press 1 for addition\n press 2 for subtraction\n press 3 or multiplication\n press 4 for division")
    option = int(input("entert your option:"))
    if option==1:
        result=a+b
        print("addition:",result)
    elif option==2:
        result=b-a
        print("subtraction:",result)
    elif option==3:
        result=a*b
        print("multiplication:",result)
    elif option==4:
        result=a/b
        print("division:",result)
    else:
        print("Invalid value")

switch()


# In[ ]:




