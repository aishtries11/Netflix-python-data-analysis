#!/usr/bin/env python
# coding: utf-8

# In[9]:


#importing the libraries
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[10]:


data= pd.read_csv(r"D:\Downloads\netflix_titles.csv")


# In[11]:


data.head()


# In[12]:


data.columns


# In[13]:


data.shape


# In[14]:


data.tail()


# In[15]:


#total values present in the dataframe at this point of time
data.size


# In[16]:


data.dtypes


# In[17]:


#indexes, columns, and data types of each column including if there are any null values
data.info()


# #### Checking if there are duplicate entries in the dataset

# In[18]:


data.shape


# In[19]:


data[data.duplicated()]
#we can see no duplicates
#if there were duplicates then use data.drop_duplicates(inplace=True)


# #### Checking for any null values

# In[20]:


data.isnull().sum()


# In[21]:


sns.heatmap(data.isnull())
#the white parts are null values
#we can observe from this heatmap that the maximum null values are in the director column.


# #### To find out cast names based on the Title

# In[22]:


data.head()


# In[23]:


data['title']


# In[24]:


#for example, I am going to search for the cast of Kota Factory
data[data['title'].str.contains('Kota Factory')]


# ### The year in which the highest number of TV shows or movies were released

# In[25]:


#checking to see what the datatypes of the columns are
data.dtypes


# In[26]:


data['release_year'].value_counts()
#we can see the year is 2018


# In[27]:


data.groupby('type').type.count()


# In[28]:


x=data['type']


# In[29]:


sns.countplot(x)


# #### Having a look at which movies were released in the year 2020

# In[30]:


data.head(2)


# In[31]:


data.groupby('release_year').release_year.count()


# In[32]:


data[(data['type']=='Movie')&(data['release_year']==2020)].head()


# ####  to show the titles of all the TV shows that were released in India only

# In[33]:


data.head(2)


# In[34]:


data[(data['type']=='TV Show')& (data['country']=='India')]['title']


# #### The top 10 directors who gave the most number of TV Shows or Movies to Netflix

# In[35]:


data.head(2)


# In[36]:


data['director'].value_counts().head(10)


# #### Show all the records where "Category is Movie and country is India" or "Country is United States"

# In[37]:


data.tail(2)


# In[ ]:





# In[38]:


data[((data['type']=='Movie' ) & (data['country']=='India')) | (data['type']=='UnitedStates')]


# #### In how many movies was Tom Cruise cast

# In[45]:


#we cant directly find using str.contains because there are Nan values in the casst column
#we will create a new dataframe without the Nan values
data2=data.dropna()


# In[46]:


data2[data2['cast'].str.contains('Tom Cruise')]


# #### WHat are the different ratings defined by Netflix?

# In[47]:


data.rating.nunique()


# In[48]:


data['rating'].nunique()


# In[49]:


data['rating'].unique()


# #### How many movies got TV-14 rating in Canada?

# In[50]:


data2.head(2)


# In[68]:


data2[(data2['country']=='Canada') & (data2['rating']=='TV-14')].shape


# #### How many TV shows got rated TV-MA in 2018?

# In[81]:


data2[(data2['type']=='TV Show')& (data2['rating']=='TV-MA') & (data2['release_year']==2018)].shape

