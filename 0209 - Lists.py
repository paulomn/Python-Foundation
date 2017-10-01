
# coding: utf-8

# # Lists

# In[1]:


listGrocery = ["eggs", "flour", "milk", "apples"]


# In[2]:


print(listGrocery)


# In[3]:


listGeneric = [12, 100, "University"]


# In[4]:


print(listGeneric)


# In[5]:


item1 = listGeneric[0]


# In[6]:


item2 = listGeneric[1]


# In[7]:


item3 = listGeneric[2]


# In[8]:


print(item1, item2, item3)


# # Updating Lists

# In[9]:


print(listGrocery[2])


# In[10]:


listGrocery[2] = "strawberry"


# In[11]:


print(listGrocery)


# # Deleting Items

# In[12]:


del listGrocery[2]


# In[13]:


print(listGrocery)


# # Matrix

# In[14]:


lists = [[1, 2, 3], [10, 14, 15], [10.1, 8.7, 2.3]]


# In[15]:


lists


# In[16]:


a = lists[0]


# In[17]:


a


# In[18]:


b = a[0]


# In[19]:


b


# In[20]:


anotherList = lists[1]


# In[21]:


anotherList


# In[22]:


value_1_0 = anotherList[0]


# In[23]:


value_1_0


# In[24]:


value_1_2 = anotherList[2]


# In[25]:


value_1_2


# # Matrix Operations

# In[26]:


lists


# In[27]:


a = lists[0][0]


# In[28]:


a


# In[29]:


b = lists[1][2]


# In[30]:


b


# In[31]:


c = lists[0][2] + 10


# In[32]:


c


# In[33]:


d = 10


# In[34]:


d


# In[35]:


e = d * lists[2][0]


# In[36]:


e


# # Concatanating Lists

# In[37]:


list_s1 = [34, 32, 56]


# In[38]:


list_s1


# In[39]:


list_s2 = [21, 90, 51]


# In[40]:


list_s2


# In[41]:


list_total = list_s1 + list_s2


# In[42]:


list_total


# # Operator IN

# In[43]:


list_test = [100, 2, -5, 3.4]


# In[44]:


print(10 in list_test)


# In[45]:


print(100 in list_test)


# # Built-in Functions

# In[46]:


len(list_test)


# In[47]:


max(list_test)


# In[48]:


min(list_test)


# In[49]:


listGrocery.append("beef")


# In[50]:


listGrocery


# In[51]:


listGrocery.append("beef")


# In[52]:


listGrocery


# In[53]:


listGrocery.count("beef")


# In[54]:


a = []


# In[55]:


type(a)


# In[56]:


a.append(10)


# In[57]:


a


# In[58]:


a.append(50)


# In[59]:


a


# In[60]:


old_list = [1, 2, 5, 10]


# In[61]:


new_list = []


# In[63]:


for item in old_list:
    new_list.append(item)


# In[64]:


new_list


# In[66]:


cities = ["Toronto", "Montreal", "Vancouver"]


# In[67]:


cities.extend(["Edmonton", "Otawa"])


# In[68]:


print(cities)


# In[69]:


cities.index("Toronto")


# In[74]:


cities.insert(2, "London")


# In[75]:


cities


# In[76]:


cities.remove("London")


# In[77]:


cities


# In[78]:


cities.reverse()


# In[79]:


cities


# In[80]:


list_sort  = [3, 4, 2, 1]


# In[81]:


list_sort.sort()


# In[82]:


list_sort

