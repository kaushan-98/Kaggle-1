#!/usr/bin/env python
# coding: utf-8

# # Strings and Dictionaries

# In[1]:


'Pluto's a planet!'


# In[2]:


'Pluto\'s a planet!'


# In[3]:


hello = "hello\nworld"
print(hello)


# In[6]:


triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello


# In[7]:


print("hello", end='')
print("pluto", end='')
print("kkk", end='')
print("jj", end='')


# In[8]:


planet = 'Pluto'
planet[0]


# In[9]:


# Slicing
planet[-3:]


# In[11]:


[char+'! ' for char in planet]


# In[12]:


planet[0] = 'B'


# In[15]:


planet[0] =='P'


# In[16]:


lanet[0] ='P'


# In[21]:


claim = "Pluto is a planet!"
claim.upper() 


# In[18]:


claim.lower()


# In[22]:


claim.index('plan')


# In[23]:


claim.startswith(planet)


# In[24]:


claim.endswith('planet')


# In[25]:


words = claim.split()
words


# In[26]:


datestr = '1956-01-31'
year, month, day = datestr.split('-')


# In[27]:


datestr.split('-')


# In[28]:


'/'.join([month, day, year])


# In[29]:


' 👏 '.join([word.upper() for word in words])


# In[30]:


planet + ', we miss you.'


# In[31]:


position = 9
planet + ", you'll always be the " + position + "th planet to me."


# In[32]:


planet + ", you'll always be the " + str(position) + "th planet to me."


# In[33]:


"{}, you'll always be the {}th planet to me.".format(planet, position)


# In[34]:


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390


# In[36]:


"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)


# In[37]:


s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)


# In[38]:


numbers = {'one':1, 'two':2, 'three':3}
numbers['one']


# In[39]:


numbers['eleven'] = 11
numbers


# In[41]:


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {ii: planet[0] for ii in planets}
planet_to_initial


# In[42]:


'Saturn' in planet_to_initial


# In[43]:


'Betelgeuse' in planet_to_initial


# In[44]:


for k in numbers:
    print("{} = {}".format(k, numbers[k]))


# In[46]:


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial


# In[47]:


# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))


# In[48]:


for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))


# In[49]:


import math

print("It's math! It has type {}".format(type(math)))


# In[51]:


print(dir(math))


# In[52]:


print("pi to 4 significant digits = {:.4}".format(math.pi))


# In[53]:


math.log(32, 2)


# In[54]:


import math as mt
mt.pi


# In[55]:


import math
mt = math


# In[56]:


from math import *
print(pi, log(32, 2))


# In[57]:


from math import *
from numpy import *
print(pi, log(32, 2))


# In[58]:


from math import log, pi
from numpy import asarray


# In[59]:


import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )


# In[60]:


# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
rolls


# In[61]:


type(rolls)


# In[62]:


print(dir(rolls))


# In[63]:


# If I want the average roll, the "mean" method looks promising...
rolls.mean()


# In[64]:


# Or maybe I just want to turn the array into a list, in which case I can use "tolist"
rolls.tolist()


# In[65]:


[3, 4, 1, 2, 2, 1] + 10


# In[66]:


rolls + 10


# In[67]:


rolls


# In[68]:


rolls <= 3


# In[69]:


xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))


# In[70]:


x[1,-1]


# In[ ]:





# In[74]:


import tensorflow as tf


# In[ ]:





# In[ ]:




