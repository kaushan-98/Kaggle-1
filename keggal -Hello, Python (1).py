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


# In[ ]:


# def mult_by_five(x):
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


# # Exercise

# In[1]:


def sign (a):
    if a < 0 :
        return -1
    elif a > 0:
        return 1
    else :
        return 0


# In[2]:


def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)


# In[11]:


def to_smash(total_candies):
   
    
    if total_candies == 1 :
        return print("Splitting", total_candies, "candy")
    
    elif total_candies > 0:
        return print("Splitting", total_candies, "candies")
    else :
        return 0
    total_candies % 3
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    #print("Splitting", total_candies, "candies")
    

to_smash(91)
to_smash(1)


# In[15]:


def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or (rain_level < 5 and have_hood) or not (rain_level > 0 and is_workday)

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

#prepared_for_weather(True,0.0,True,True)

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Check your answer
#q3.check()


# In[16]:


def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return is_negative(number)

    


# In[17]:


def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and  not mustard and not onion
    #pass
wants_all_toppings(True,True,True)
# Check your answer


# In[18]:


return not ketchup and not mustard and not onion
We can also "factor out" the nots to get:

return not (ketchup or mustard or onion)


# In[19]:


def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)
    pass


# # Lists

# In[20]:


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# In[21]:


planets 


# In[22]:


planets[0]
planets[-1]
planets[-2]
planets[0:3]
planets[:3]
# All the planets except the first and last
planets[1:-1]
# The last 3 planets
planets[-3:]


# In[23]:


planets[3] = 'Malacandra'
planets


# In[24]:


planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)


# In[25]:


len(planets)


# In[26]:


sorted(planets)


# In[27]:


primes = [2, 3, 5, 7]
sum(primes)


# In[28]:


max(primes)


# In[29]:


x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)


# In[30]:


c = 12 + 3j
print(c.imag)


# In[31]:


x.bit_length


# In[32]:


x.bit_length


# In[34]:


help(x.bit_length)


# In[35]:


planets.append('Pluto')


# In[36]:


planets


# In[38]:


planets.pop() #remove last element of planet


# In[39]:


planets.index('Earth')


# In[40]:


"Earth" in planets


# In[41]:


x = 0.125
x.as_integer_ratio()


# In[42]:


numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)


# In[43]:


a = 1
b = 0
a, b = b, a
print(a, b)


# In[44]:


def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
        #print (L[1])
    else:
        return L[1]
        #print(non)


# In[45]:


def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]
    pass


# In[46]:


def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    c = racers[0]
    racers[0] = racers[-1]
    racers[-1] = c 
    pass

# Check your answer
q3.check()


# In[48]:


a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [len(a),len(b),len(c),len(d)]
#a = 3
#b = 2
#c = 0
#d = 2

# Check your answer


# # Loops and List Comprehensions

# In[49]:


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line


# In[54]:


multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product


# In[55]:


s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')


# In[56]:


for i in range(5):
    print("Doing important work. i =", i)


# In[57]:


i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increase the value of i by 1


# In[58]:


squares = [n**2 for n in range(10)]
squares


# In[59]:


squares = []
for n in range(10):
    squares.append(n**2)
squares


# In[60]:


short_planets = [planet for planet in planets if len(planet) < 6]
short_planets


# In[61]:


# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets


# In[62]:


[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]


# In[63]:


[32 for planet in planets]


# In[64]:


def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
             return True
    return False
    pass
#def menu_is_boring()


# In[ ]:




