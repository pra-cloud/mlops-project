#!/usr/bin/env python
# coding: utf-8

# ## First Innings Score Prediction

# In[1]:


# Importing libraries
import pandas as pd
import numpy as np

# Loading ipl dataset
df = pd.read_csv('ipl.csv')


# In[2]:

# View ipl dataset
df.head()


# In[3]:


# ---  Data Cleaning process ---
# Removing unwanted Features
columns_to_remove = ['mid', 'venue', 'batsman', 'bowler', 'striker', 'non-striker']
df.drop(labels=columns_to_remove, axis=1, inplace=True)


# In[4]:


df.head()


# In[5]:


df['bat_team'].unique()


# In[6]:


# --- Keeping only consistent teams from 2008 to 2017 ---
consistent_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                    'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                    'Delhi Daredevils', 'Sunrisers Hyderabad']


# In[7]:


df = df[(df['bat_team'].isin(consistent_teams)) & (df['bowl_team'].isin(consistent_teams))]


# In[8]:


# Removing the first 5 overs data in every match 
df = df[df['overs']>=5.0]


# In[9]:


df.head()


# In[10]:

# List down Batting and Bowling Team: 

print(df['bat_team'].unique())
print(df['bowl_team'].unique())


# In[11]:


# Converting the 'date' feature from string into datetime object
from datetime import datetime
df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))


# In[12]:


# --- Data Preprocessing ---
# Converting categorical features using OneHotEncoding method
encoded_df = pd.get_dummies(data=df, columns=['bat_team', 'bowl_team'])


# In[13]:


encoded_df.head()


# In[14]:


encoded_df.head()


# In[15]:


encoded_df.columns


# In[16]:


# Rearranging the columns
encoded_df = encoded_df[['date', 'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils', 'bat_team_Kings XI Punjab',
              'bat_team_Kolkata Knight Riders', 'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
              'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
              'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils', 'bowl_team_Kings XI Punjab',
              'bowl_team_Kolkata Knight Riders', 'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
              'bowl_team_Royal Challengers Bangalore', 'bowl_team_Sunrisers Hyderabad',
              'overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5', 'total']]


# In[17]:


# Splitting the data into train and test dataset
X_train = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year <= 2016]
X_test = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year >= 2017]


# In[18]:


y_train = encoded_df[encoded_df['date'].dt.year <= 2016]['total'].values
y_test = encoded_df[encoded_df['date'].dt.year >= 2017]['total'].values


# In[19]:


# Removing the 'date' feature
X_train.drop(labels='date', axis=True, inplace=True)
X_test.drop(labels='date', axis=True, inplace=True)


# In[20]:


# --- Model Building ---
# ## Lasso Regression

# In[31]:


from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV


# In[32]:


lasso=Lasso()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40]}
lasso_regressor=GridSearchCV(lasso,parameters,scoring='neg_mean_squared_error',cv=5)

# fit the model
lasso_regressor.fit(X_train,y_train)


# In[33]:


prediction=lasso_regressor.predict(X_test)


# In[34]:

# Plot a histogram to make sure it looks normally distributed.
import seaborn as sns
sns.distplot(y_test-prediction)


# In[35]:


from sklearn import metrics

# Checking error
print('MAE:', metrics.mean_absolute_error(y_test, prediction))
print('MSE:', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))


# In[38]:


# Creating a pickle file to save model.
import pickle
filename = 'ipl_lasso-model.pkl'
pickle.dump(lasso_regressor, open(filename, 'wb'))


# In[ ]:




