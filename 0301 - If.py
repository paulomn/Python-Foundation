
# coding: utf-8

# # If Conditional

# In[1]:


if 5 > 2:
    print("Python works!")


# In[2]:


if 1 > 2:
    print("Python works!")
else:
    print("It really works!")


# In[3]:


6 > 3


# In[4]:


3 > 7


# In[5]:


4>=4


# In[6]:


if 5 == 5:
    print("Python works!")


# In[7]:


if True:
    print("Python works!")


# # Nested Conditionals

# In[8]:


idade = 18
if idade > 17:
    print("You can drive!")


# In[9]:


name = "Bob"
if name == "Bob":
    if idade > 13:
        print("OK")
    else:
        print("NOK")


# In[11]:


if idade >=13 and name == "Bob":
    print("OK")


# In[12]:


if (idade >=23) or (name == "Bob"):
    print("OK")


# # Elif

# In[14]:


day = "Wednesday"
if day == "Monday":
    print("Bad wheather")
elif day == "Tuesday":
    print("Good wheather")
else:
    print("Bad wheather again")


# # Conditional Operators

# In[17]:


subject = input("Type the name of the subject: ")
mark = input("Type your mark: ")

if (subject == "Math" and mark >= "50"):
    print("You passed!")
else:
    print("You fail!")


# # Placeholders

# In[19]:


print("You has been approved in %s with the mark %r" %(subject, mark))

