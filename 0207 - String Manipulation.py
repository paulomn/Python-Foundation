
# coding: utf-8

# # String Generation

# In[1]:


'Hi'


# In[2]:


'This is a string in Python'


# In[3]:


"This is another string"


# In[4]:


"Testing string 'control'"


# # Printing Strings

# In[5]:


print('Testing strings in Python')


# In[7]:


print('Testing \nstrings \nin \nPython')


# In[8]:


print('\n')


# # String Index

# In[9]:


s = "Data Science Academy"


# In[10]:


print(s)


# In[11]:


s[0]


# In[12]:


s[1]


# In[13]:


s[2]


# # String Slicing

# In[14]:


s[1:]


# In[15]:


s


# In[16]:


s[:3]


# In[17]:


s[:]


# In[18]:


s[-1]


# In[19]:


s[:-1]


# In[20]:


s[::1]


# In[21]:


s[::2]


# In[22]:


s[::-1]


# # Strings Properties

# In[23]:


s


# In[24]:


s[0] = 'x'


# In[25]:


s= s + ' é a melhor maneira de aprender.'


# In[26]:


s


# In[27]:


character = 'w'


# In[28]:


character * 3


# # Built-in Functions

# In[29]:


s


# In[30]:


s.upper()


# In[31]:


s.lower()


# In[32]:


s.split()


# In[34]:


s.split('y')


# In[35]:


s = 'hello!'


# In[36]:


s.capitalize()


# In[37]:


s.count('l')


# In[38]:


s.find('e')


# In[40]:


s.center(20, 'e')


# In[41]:


s.isalnum()


# In[42]:


s.isalpha()


# In[43]:


s.islower()


# In[44]:


s.isspace()


# In[45]:


s.endswith('!')


# In[46]:


s.partition('!')


# # String Comparison

# In[47]:


print('Python' == 'R')


# In[48]:


print('Python' == 'Python')

