
# coding: utf-8

# In[1]:


#Exercise 1


# In[2]:


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[3]:


print(list1)


# In[4]:


#Exercise 2


# In[5]:


list2 = ["Milk", "Eggs", "Beef", "Flour", "Onions"]


# In[6]:


print(list2)


# In[11]:


#Exercise 3


# In[7]:


string1 = "Ptyhon is "


# In[8]:


string2 = "powerful"


# In[9]:


string3 = string1 + string2


# In[10]:


print(string3)


# In[12]:


#Exercise 4


# In[13]:


tuple1 = (1, 2, 2, 3, 4, 4, 4, 5)


# In[15]:


tuple1.count(4)


# In[16]:


#Exercise 5


# In[17]:


dict1 = {"k1":1, "k2":2, "k3":3}


# In[19]:


print(dict1)


# In[23]:


#Exercise 6


# In[21]:


dict1["k4"] = 4


# In[22]:


print(dict1)


# In[24]:


#Exercise 7


# In[25]:


fileName = open("names.txt", "w")


# In[27]:


fileName.write("John, Paul, Ringo, George, Harrisson")


# In[28]:


fileName.close()


# In[ ]:


#Exercise 8


# In[32]:


fileName = open("names.txt", "r")


# In[33]:


print(fileName.read())


# In[34]:


fileName.close()


# In[36]:


#Exercise 9


# In[35]:


dict2 = {}


# In[37]:


#Exercise 10


# In[38]:


import pandas as pd


# In[39]:


file_name = "salaries.csv"


# In[40]:


df = pd.read_csv(file_name)


# In[41]:


df.tail()

