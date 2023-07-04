#!/usr/bin/env python
# coding: utf-8

# In[45]:


#import numpy as np


# In[46]:


import pandas as pd


# In[47]:


import matplotlib.pyplot as plt


# In[48]:


import seaborn as sns


# In[95]:


#%matplotlib inline


# In[50]:


df = pd.read_csv('911.csv')


# In[51]:


df.info()


# In[52]:


df.head()


# In[53]:


#top 10 zip calls


# In[54]:


df['zip'].value_counts().head(10)


# In[55]:


#top 5 townships


# In[56]:


df['twp'].value_counts().head(5)


# In[57]:


df['title'].nunique()


# In[58]:


x=df['title'].iloc[0]


# In[59]:


x


# In[60]:


y=x.split(':')[0]


# In[61]:


df['Reason']=df['title'].apply(lambda title: title.split(':')[0])


# In[62]:


#df['Reason']=df['title'].apply(lambda title:y)


# In[63]:


df['Reason']


# In[64]:


df['Reason'].value_counts().head(1)


# In[65]:


sns.countplot(x='Reason',data=df,palette='viridis')


# In[66]:


type(df['timeStamp'].iloc[0])


# In[67]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])


# In[68]:


type(df['timeStamp'].iloc[0])


# In[69]:


time = df['timeStamp'].iloc[0]
time.hour


# In[70]:


time


# In[71]:


df['Hour']=df['timeStamp'].apply(lambda time:time.hour)
df['Month']=df['timeStamp'].apply(lambda time:time.month)
df['Day of Week']=df['timeStamp'].apply(lambda time:time.dayofweek)


# In[72]:


df['Hour']


# In[73]:


df['Month']


# In[74]:


df['Day of Week']


# In[75]:


df.head()


# In[78]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week']=df['Day of Week'].map(dmap)


# In[79]:


df['Day of Week']


# In[80]:


df.head()


# In[86]:


sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
#relocating legend
plt.legend(bbox_to_anchor=(1.05,1), loc=2 ,borderaxespad=0. )


# In[87]:


sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05,1), loc=2 ,borderaxespad=0. )


# In[90]:


byMonth = df.groupby('Month').count()


# In[92]:


byMonth.head()


# In[96]:


byMonth['lat'].plot()


# In[97]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[98]:


t=df['timeStamp'].iloc[0]


# In[99]:


t


# In[100]:


t.date()


# In[101]:


df['Date']=df['timeStamp'].apply(lambda t:t.date())


# In[102]:


df['Date']


# In[104]:


df.head()


# In[110]:


df.groupby('Date').count()['lat'].plot()
plt.tight_layout()


# In[113]:


df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[114]:


df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
plt.tight_layout()


# In[115]:


df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout()


# In[122]:


dayHour=df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour


# In[132]:


sns.heatmap(dayHour,cmap='viridis')
plt.figure(figsize=(12,6))


# In[137]:


sns.clustermap(dayHour,cmap='coolwarm')


# In[134]:


dayMonth=df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth


# In[135]:


sns.heatmap(dayMonth,cmap='viridis')


# In[136]:


sns.clustermap(dayMonth,cmap='viridis')


# In[ ]:




