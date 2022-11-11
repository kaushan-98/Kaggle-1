#!/usr/bin/env python
# coding: utf-8

# # Basic Data Exploration

# In[1]:


import pandas as pd


# In[2]:


# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()
Rooms	Price


# In[3]:


# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex2 import *
print("Setup Complete")


# In[4]:


import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)


# Call line below with no argument to check that you've loaded the data correctly
step_1.check()


# In[5]:


# What is the average lot size (rounded to nearest integer)?
avg_lot_size = 10517

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 2022 - 2010

# Checks your answers
step_2.check()


# In[6]:


import pandas as pd

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns


# In[7]:


# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)


# In[8]:


y = melbourne_data.Price


# # Your First Machine Learning Model

# In[1]:


import pandas as pd

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns


# In[2]:


y = melbourne_data.Price


# In[3]:


# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)


# In[ ]:


y = melbourne_data.Price


# In[4]:


melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']


# In[ ]:


X = melbourne_data[melbourne_features]


# In[ ]:


X.describe()


# In[ ]:


X.head()


# In[ ]:


from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)


# In[ ]:


print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))


# # Model Validation

# In[5]:


# Data Loading Code Hidden Here
import pandas as pd

# Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)


# In[6]:


from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)


# In[7]:


from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))


# # Exercise: Model Validation
# 

# In[2]:


#You've built a model.


# In[ ]:


# Code you have previously used to load data
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Specify Model
iowa_model = DecisionTreeRegressor()
# Fit Model
iowa_model.fit(X, y)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex4 import *
print("Setup Complete")


# In[ ]:


# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split

# fill in and uncomment
#train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
#train_X, val_X, train_y, val_y = train_test_split(X,y, random_state=1)
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)


# In[ ]:


# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)


# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)


# In[ ]:


# Predict with all validation observations
#val_predictions = ____
val_predictions = iowa_model.predict(val_X)


# In[3]:


# print the top few validation predictions
print(val_predictions)
# print the top few actual prices from validation data
print(val_y)


# In[ ]:


from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_y, val_predictions)


# In[ ]:




