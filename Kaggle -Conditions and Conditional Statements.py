#!/usr/bin/env python
# coding: utf-8

# # Conditions and Conditional Statements

# In[1]:


def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message


# In[3]:


print(evaluate_temp(37))
print(evaluate_temp(39))


# # "if ... else" statements

# In[4]:


def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message


# In[5]:


print(evaluate_temp_with_else(37))


# # "if ... elif ... else" statements

# In[6]:


def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message


# In[9]:


evaluate_temp_with_elif(36)


# In[10]:


evaluate_temp_with_elif(34)


# In[11]:


def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed


# In[12]:


ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)


# # Example - Multiple "elif" statements

# In[13]:


def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose


# In[15]:


get_dose(5.1)


# 
# # Q1

# In[25]:


def get_grade(score):
    if score >= 90:
        score = "A"
    
    elif score >= 80:
        score = "B"
    
    elif score >=70:
        score = "C"
   
    elif score >=60:
        score = "D" 
    else:
        score = "F"
    return score

get_grade(99)


# # Q2

# In[29]:


def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10*len(engraving)
    else:
        cost = 50 + 7*len(engraving)
    return cost

cost_of_project("14", True)


# # Q3

# In[30]:


def get_water_bill(num_gallons):
    if num_gallons > 30001:
        bill = 10* flot(num_gallons/1000)
    
    elif get_water_bill > 22001:
        bill = 7* flot(num_gallons/1000)
    elif get_water_bill > 22001:
        bill = 6* flot(num_gallons/1000)
    else:
        bill = 5* flot(num_gallons/1000)
    return num_gallons


num_gallons(50000)  

#incorrect


# In[31]:


def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = 5 * float(num_gallons/1000) 
    elif num_gallons <= 22000:
        bill = 6 * float(num_gallons/1000)
    elif num_gallons <= 30000:
        bill = 7* float(num_gallons/1000)
    else:
        bill = 10 * float(num_gallons/1000)
    return bill
get_water_bill(50000)


# In[32]:


def get_phone_bill(gb):
    if gb<= 15:
        bill =100
    else:
        bill = 100 + (float( gb -15))*1000*0.1
    return bill
get_phone_bill(16)


# # Q5

# In[ ]:




