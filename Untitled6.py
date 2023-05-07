#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests


# In[27]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"


# In[28]:


df = pd.read_html(url, header=0)


# In[29]:


df[1]


# In[31]:


gme_revenue = df[1]


# In[32]:


gme_revenue.columns


# In[33]:


gme_revenue.rename(columns = {'GameStop Quarterly Revenue(Millions of US $)':'Date', 'GameStop Quarterly Revenue(Millions of US $).1':'Revenue'}, inplace=True)


# In[34]:


gme_revenue.columns


# In[35]:


gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")


# In[36]:


gme_revenue.dropna(inplace=True)


# In[37]:


gme_revenue.tail(5)


# In[38]:


gme_revenue['Date'] = pd.to_datetime(gme_revenue['Date'])


# In[39]:


plt.plot(gme_revenue['Date'], gme_revenue['Revenue'])


# In[41]:





# In[ ]:




