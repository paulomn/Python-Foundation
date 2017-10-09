
# coding: utf-8

# # Range

# In[1]:


for i in range(50, 101, 2):
    print(i)


# In[6]:


for i in range(3, 6):
    print(i)


# In[5]:


for i in range(0, 20, -2):
    print(i)


# In[7]:


list = ["Strawberry", "Banana", "Apple", "Grape"]
listLength = len(list)

for i in range(0, listLength):
    print(list[i])


# In[8]:


type(range(0, 3))

