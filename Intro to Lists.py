#!/usr/bin/env python
# coding: utf-8

# # Intro to Lists

# In[1]:


flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)


# In[2]:


print(len(flowers_list))


# In[3]:


print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])
print("Last entry:", flowers_list[9]) #9


# In[5]:


print("First three entries:", flowers_list[:3])#  0,1,2
print("Final two entries:", flowers_list[-2:]) #       -2 ,-1
print("Final two entries:", flowers_list[-3:-1]) #  -3,-2


# In[6]:


flowers_list.remove("globe thistle")
print(flowers_list)


# In[7]:


flowers_list.append("snapdragon")
print(flowers_list)


# In[8]:


hardcover_sales = [139, 128, 172, 139, 191, 168, 170]


# In[9]:


print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])


# In[10]:


print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))


# In[11]:


print("Total books sold in one week:", sum(hardcover_sales))


# In[12]:


print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)


# # Exercise

# 
# # Q1

# In[17]:


# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
letters = alphabet.split(".")
formatted_address = address.split(",")

# Do not change: Check your answer


# In[18]:


test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(test_liked)


# In[22]:



def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = len(list_liked)/8
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])


# In[ ]:




