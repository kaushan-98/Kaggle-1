#!/usr/bin/env python
# coding: utf-8

# # Hello, Python

# In[1]:


spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)


# In[2]:


print(5 / 2)
print(6 / 2)


# In[3]:


print(5 // 2)
print(6 // 2)


# # Exercise

# In[8]:


########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]

######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

######################################################################
tmp = a
a = b
b = tmp

#or
#a, b = b, a
# Check your answer


# # Getting Help

# In[9]:


help(round)


# In[10]:


help(round(-2.01))


# # Defining functions

# In[11]:


def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


# In[13]:


least_difference(1,2,3)


# In[14]:


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)


# In[15]:


mystery = print()
print(mystery)


# In[16]:


print(1, 2, 3, sep=' < ')


# In[17]:


print(1, 2, 3)


# In[18]:


def greet(who="Colin"):
    print("Hello,", who)
    
greet()# defualt
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")


# In[20]:


def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))
print(call(mult_by_five, 1),squared_call(mult_by_five, 1), sep='\n', # '\n' is the newline character - it starts a new line)


# In[22]:


def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',max(100, 51, 14),'Which number is the biggest modulo 5?', max(100, 51, 14, key=mod_5),sep='\n',)


# In[26]:


def to_smash(total_candies, n_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n_friends
to_smash(50,4)


# In[27]:


# ruound_to_two_places(9.9999)
x = 9.9999
print(round(x, 2))


# In[28]:


x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))


# In[29]:


def f(x):
    y = abs (f(x))
    return y


print(y)


# In[ ]:




