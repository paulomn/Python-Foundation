
# coding: utf-8

# # Dictionary

# In[1]:


students_list = ["Peter", 24, "Fernand", 22, "Tan", 25, "Chris", 25]


# In[2]:


students_list


# In[3]:


students_dic = {"Peter":25, "Fernand":22, "Tan":26, "Chris":25}


# In[5]:


students_dic["Peter"]


# In[6]:


students_dic["Peter"] = 23


# In[7]:


students_dic["Peter"]


# In[8]:


students_dic["Tan"]


# In[10]:


students_dic.clear()


# In[11]:


del students_dic


# In[12]:


students_dic = {"Peter":25, "Fernand":22, "Tan":26, "Chris":25}


# In[13]:


len(students_dic)


# In[14]:


students_dic.keys()


# In[15]:


students_dic.values()


# In[16]:


students_dic.items()


# In[18]:


students2_dic = {"Mary":27, "Erik":28, "Elton":26}


# In[19]:


students2_dic


# In[20]:


students_dic.update(students2_dic)


# In[21]:


students_dic


# In[22]:


empty_dic = {}


# In[23]:


empty_dic["Key1"] = 2


# In[24]:


empty_dic


# In[25]:


empty_dic[10] = 5


# In[26]:


empty_dic[8.2] = "Hi"


# In[27]:


empty_dic


# # Dictionary of Lists

# In[28]:


list_dic = {"key1":1230, "key2":[22, 453, 73], "key3":["milk", "apple", "potatoes"]}


# In[29]:


list_dic


# In[30]:


list_dic["key3"][0].upper()


# In[31]:


calc = list_dic["key2"][0] - 2


# In[32]:


calc


# In[33]:


list_dic["key2"][0] -= 2


# In[34]:


list_dic


# # Nested Dictionaries

# In[35]:


nested_dic = {"key1": {"key2": {"key3": "Nested Dictionary"}}}


# In[36]:


nested_dic["key1"]["key2"]["key3"]

