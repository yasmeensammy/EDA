#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


user_input_path = input("[REQUIRED] Please Enter data file path: ")
dataset_extension = user_input_path.split('.')[-1]

if dataset_extension in ['xlsx', 'xls', 'xlt']:
    df = pd.read_excel(user_input_path)
elif dataset_extension == 'csv':
    df = pd.read_csv(user_input_path)
elif dataset_extension == 'tsv':
    df = pd.read_csv(user_input_path, sep='\t')
else:
    print(f'UnRechognized file extinsion {dataset_extension} try again with supported file.')
    print('Supported extensions is: .xlsx, .xls, .xlt, .csv, .tsv')
    


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.shape


# In[7]:


df.dtypes


# In[8]:


df.count()


# In[9]:


df.describe()


# In[10]:


df.nunique(axis=0)


# In[11]:


df.duplicated().sum()


# In[12]:


df.isnull().sum()


# In[13]:


plt.figure(figsize = (10,6))
plt.title("Missing values in Each Column\n", size = 15)
sns.heatmap(df.isnull(), yticklabels=False, cbar=False);


# In[14]:


df.replace(np.nan,'0',inplace = True)


# In[15]:


df.isnull().sum()


# In[16]:


plt.figure(figsize = (10,6))
plt.title("Missing values in Each Column\n", size = 15)
sns.heatmap(df.isnull(), yticklabels=False, cbar=False);


# In[17]:


for column in df.select_dtypes(include='object'):
    if df[column].nunique() < 10:
        display(df.groupby(column).mean())


# In[18]:


df.corr()


# In[19]:


plt.figure(figsize=(15,8))
sns.heatmap(df.corr(), cmap="YlGnBu", annot=True);


# In[20]:


import pandas_profiling as pp 


# In[21]:


import warnings
warnings.filterwarnings('ignore')


# In[22]:


pp.ProfileReport(df)


# In[23]:


df.describe(include='object')


# In[24]:


categorical = []
for column in df.select_dtypes(include='object'):
    if df[column].nunique() <= 10:
        categorical.append(column)

print(categorical)
fig,axs=plt.subplots(len(categorical),1,)

for i, column in enumerate(categorical):
    sns.countplot(y=column, data=df,ax=axs[i])

plt.show()


# In[25]:


df.describe(exclude='object')


# In[26]:


boolean = []
for column in df.select_dtypes(exclude='object'):
    if df[column].nunique() <= 10:
        boolean.append(column)

print(boolean)
fig,axs=plt.subplots(len(boolean),1,)

for i, column in enumerate(boolean):
    sns.countplot(y=column, data=df,ax=axs[i])

plt.show()


# In[27]:


non_cat = []
for column in df.select_dtypes(exclude='object'):
    if df[column].nunique() > 1:
        non_cat.append(column)

print(non_cat)
fig,axs=plt.subplots(len(non_cat),1,)

for i, column in enumerate(non_cat):
    sns.countplot(y=column, data=df,ax=axs[i])

plt.show()


# In[ ]:





# In[ ]:




