
# coding: utf-8

# In[10]:


from pandas_datareader import data


# In[13]:


aapl = data.DataReader('AAPL', 'yahoo', '2018-01-01')


# In[16]:


gogl = data.DataReader('GOOGL', 'yahoo', '2018-01-01')


# In[17]:


amzn = data.DataReader('AMZN', 'yahoo', '2018-01-01')


# In[21]:


aapl.to_csv('aapl.csv',index=False)
gogl.to_csv('google.csv', index = False)
amzn.to_csv('amazn.csv', index = False)

