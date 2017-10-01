
# coding: utf-8

# # Tuples

# In[1]:


tuple1 = ("Matemática", 23, "Gatos")


# In[2]:


tuple1


# In[3]:


tuple1.append("Chocolate")


# In[4]:


del tuple1["Gatos"]


# In[6]:


tuple1 = ("Chocolate")


# In[7]:


tuple1.count()


# In[8]:


len(tuple1)


# In[9]:


tuple1


# In[11]:


tuple1[:1]


# In[12]:


del tuple1


# In[13]:


tuple1 = ("A", "B", "C", "D")


# In[14]:


tupleToList = list(tuple1)


# In[15]:


tupleToList


# In[16]:


tupleToList.append("E")


# In[17]:


tuple1 = tuple(tupleToList)


# In[18]:


tuple1

