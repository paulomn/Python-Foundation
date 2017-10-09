
# coding: utf-8

# # While

# In[1]:


counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1


# In[1]:


x = 0

while x < 10:
    print("Iteraction value: ", x)
    x += 1
else:
    print("Loop finished!")


# In[5]:


counter = 0

while counter < 100:
    if counter == 4:
        break
    else:
        pass
        print(counter)
    counter += 1


# In[6]:


for verifier in "Python":
    if verifier == "h":
        continue
    print(verifier)

