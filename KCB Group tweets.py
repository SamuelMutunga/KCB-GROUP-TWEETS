#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install snscrape


# In[7]:


import pandas as pd
from tqdm.notebook import tqdm


# In[8]:


import snscrape.modules.twitter as sntwitter


# In[9]:


scraper=sntwitter.TwitterSearchScraper('#python')


# In[23]:


pip install ntscraper


# In[11]:


from ntscraper import Nitter


# In[12]:


scraper=Nitter()


# In[13]:


tweets=scraper.get_tweets('KCBGroup',mode='user', number=50)


# In[14]:


tweets


# In[28]:


for tweet in tweets['tweets']:
    print(tweet)
    print('.........Next Tweet.......')


# In[15]:


final_tweets=[]
for tweet in tweets['tweets']:
    data=[tweet['link'],tweet['text'],tweet['date'],tweet['stats']['likes'],tweet['stats']['comments']]
    final_tweets.append(data)


# In[16]:


print(final_tweets)


# In[17]:


data=pd.DataFrame(final_tweets, columns=['link','text','date','no_of_likes','no_of_tweets'])


# In[18]:


data


# In[19]:


def get_tweets(name,modes,no):
    tweets=scraper.get_tweets(name,mode=modes,number=no)
    final_tweets=[]
    for tweet in tweets['tweets']:
       data=[tweet['link'],tweet['text'],tweet['date'],tweet['stats']['likes'],tweet['stats']['comments']]
       final_tweets.append(data)
    data=pd.DataFrame(final_tweets, columns=['link','text','date','no_of_likes','no_of_tweets'])
    return data


# In[20]:


data=get_tweets('KCBGroup','user',50)


# you can get user,term or hashtag

# In[21]:


import numpy as np
import pandas as np
import csv


# In[22]:


data = get_tweets('KCBGroup','user',50)
df = pd.DataFrame(data=data)
df.to_csv("data.csv")


# In[23]:


data


# In[24]:


pip install xlsxwriter


# In[31]:


pd.DataFrame(data).to_excel("C:/Users/Hp/OneDrive/Documents/KCB.xlsx")


# In[32]:


with pd.ExcelWriter('C:/Users/Hp/OneDrive/Documents/coop.xlsx',engine='xlsxwriter') as writer:  
 data.to_excel(writer, 'KCBGroup tweets')


# In[33]:


df = pd.read_csv("data.csv",index_col=0)
print(df)


# In[28]:


data=df
data


# In[29]:


df


# In[34]:


scraper.get_profile_info('KCBGroup')


# In[36]:


import openpyxl


# In[37]:


new_data=data.to_excel("data.xlsx", sheet_name="tweets", index=False)


# In[38]:


df=data.to_excel("data.xlsx")


# In[ ]:




