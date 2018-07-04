
# coding: utf-8

# In[2]:


text="""******************************************************************
                            Invoice
******************************************************************
Customer-ID: sm-LK0080145
Inv-ID: inv-00001
Dated: Mar 31 2018
From: Space Mechanics Inc.
To: Starfleet Interplanatory HQ
Amount: SR 7650/-
SGST: SR 500/-
Total: SR 8150/-
InWords: Space Rupees Eight thousand one hundred fifty only

Items
1) Matter antimatter fusion controller, 2000, 200
2) External inertial damper, 3100, 180
3) Type X phaser, 500, 35
4) 2MW Fusion reactor, 1200, 85
5) Transporter base dial, 850"""


# In[3]:


text=text.split(":")


# In[4]:


text[0]=text[0].split()[3]


# In[5]:


items=text[(len(text)-1)].split("Items")[1]
text[(len(text)-1)]=text[(len(text)-1)].split("Items")[0]


# In[6]:


items=items.split("\n")[1:]


# In[8]:


df=[]
for i in range(0,len(text)):
    if not("\n" in text[i]) :
        df.append(text[i])
    else :
        df.append(text[i].split("\n"))


# In[10]:


z="\n".join(text)


# In[11]:


z=z.split("\n")[:-2]


# In[13]:


try:
    from itertools import izip as zip
except ImportError: # will be 3.x series
    pass


# In[14]:


i = iter(z)


# In[15]:


b = dict(zip(i, i))


# In[16]:


import csv


# In[35]:


with open(str(b["Customer-ID"]+b["Inv-ID"])+".csv", 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, b.keys())
    w.writeheader()
    w.writerow(b)


# In[19]:


for i in range(0,len(items)):
    items[0].split(",")[0][3:]


# In[20]:


j=[]
for i in items:
    j.append(i[3:].split(","))


# In[21]:


with open("items.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(j)


# In[29]:


import pandas as pd
df=pd.read_csv("items.csv",header=None)


# In[31]:


df.columns = ["Item Name","Price","Qty"]


# In[40]:


df.to_csv(str(b["Customer-ID"]+b["Inv-ID"])+"_items.csv",encoding="utf-8")

