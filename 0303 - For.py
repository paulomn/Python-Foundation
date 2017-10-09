
# coding: utf-8

# # Loop For

# In[1]:


tuple1 = (2, 3, 4)
for i in tuple1:
    print(i)


# In[3]:


shopList = ["Milk", "Fruit", "Beef"]
for i in shopList:
    print(i)


# In[4]:


for count in range(0, 5):
    print(count)


# In[5]:


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list:
    if num % 2 == 0:
        print(num)


# In[6]:


for i in range(0, 101, 2):
    print(i)


# In[7]:


for char in "Python is amazing":
    print(char)


# # Nested For

# In[8]:


for i in range(0, 5):
    for a in range(0, 5):
        print(a)


# In[9]:


lists = [[1, 2, 3], [10, 14, 15], [10.1, 8.7, 2.3]]
for value in lists:
    print(value)


# In[10]:


list = [5, 6, 10, 13, 17]
count = 0
for item in list:
    count += 1
    
print(count)


# In[11]:


list = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
firstLine = list[0]
count = 0
for column in firstLine:
    count += 1
    
print(count)


# In[13]:


dict = {"k1": "Python", "k2": "R", "k3": "Scala"}
for item in dict:
    print(item)


# In[15]:


for k, v in dict.items():
    print(k, v)

