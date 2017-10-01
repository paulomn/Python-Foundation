
# coding: utf-8

# # Reading Files

# In[5]:


file1 = open("file-dsa.txt", "r")


# In[6]:


print(file1.read())


# In[7]:


print(file1.tell())


# In[8]:


print(file1.seek(0, 0))


# In[9]:


print(file1.read(10))


# # Writing Files

# In[12]:


file2 = open("file-dsa.txt", "w")


# In[13]:


print(file2.read())


# In[14]:


file2.write("Testing Python writing...")


# In[15]:


file2.close()


# In[16]:


file2 = open("file-dsa.txt", "r")


# In[17]:


print(file2.read())


# In[18]:


file2.close()


# In[19]:


file2 = open("file-dsa.txt", "a")


# In[20]:


file2.write("Appending content...")


# In[21]:


file2.close()


# In[22]:


file2 = open("file-dsa.txt", "r")


# In[23]:


print(file2.read())


# In[24]:


file2.close()


# # Creating a File Dinamically

# In[25]:


fileName = input("Digite o nome do arquivo: ")


# In[26]:


fileName = fileName + ".txt"


# In[27]:


file3 = open(fileName, "w")


# In[28]:


file3.write("Python is a powerful language!")


# In[29]:


file3.close()


# In[30]:


file3 = open(fileName, "r")


# In[31]:


print(file3.read())


# In[32]:


file3.close()


# # Opening Datasets

# In[38]:


file4 = open("salaries.csv", "r")


# In[39]:


data = file4.read()


# In[40]:


rows = data.split("\n")


# In[41]:


print(rows)


# # Splitting Columns

# In[42]:


file5 = open("salaries.csv", "r")


# In[43]:


data = file5.read()


# In[44]:


rows = data.split("\n")


# In[45]:


full_data = []


# In[47]:


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


# In[48]:


print(full_data)


# # Couting Rows

# In[49]:


file6 = open("salaries.csv", "r")


# In[50]:


data = file6.read()


# In[51]:


rows = data.split("\n")


# In[52]:


full_data = []


# In[53]:


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


# In[54]:


count = 0
for row in full_data:
    count += 1


# In[55]:


print(count)


# # Couting Columns

# In[56]:


file7 = open("salaries.csv", "r")


# In[57]:


data = file7.read()


# In[58]:


rows = data.split("\n")


# In[59]:


full_data =[]


# In[60]:


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


# In[61]:


first_row = full_data[0]


# In[66]:


count = 0
for column in first_row:
    count += 1


# In[67]:


print(count)


# # Writing Files through the Jupyter Notebook

# In[69]:


get_ipython().run_cell_magic('writefile', 'fileJupyter.txt', 'Python is a powerful language')


# In[70]:


file8 = open("fileJupyter.txt", "r")


# In[71]:


file8.read()


# In[72]:


file8.read()


# In[73]:


file8.seek(0, 0)


# In[74]:


file8.read()


# # Importing with Pandas

# In[75]:


import pandas as pd


# In[78]:


file_name = "salaries.csv"


# In[79]:


df = pd.read_csv(file_name)


# In[80]:


df.head()

