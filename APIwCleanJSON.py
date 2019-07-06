#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
my_url = 'https://api.nytimes.com/svc/archive/v1/1972/5.json?api-key=1QRV6OWfH84L1K0TynvBBwg5ztvYQpUI'
r = requests.get(my_url)
x = json.loads(r.text)
x['copyright']
'Copyright (c) 2013 The New York Times Company.  All Rights Reserved.'
for doc in x['response']['docs']:
    print(doc['headline']['main'])


# In[ ]:





# In[ ]:




