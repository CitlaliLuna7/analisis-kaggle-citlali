#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

df = pd.read_csv('datos_limpios.csv')

df.head()


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df = df.drop_duplicates()

num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

df.isnull().sum()


# In[10]:


df.to_csv('datos_limpios.csv', index=False)


# In[ ]:




