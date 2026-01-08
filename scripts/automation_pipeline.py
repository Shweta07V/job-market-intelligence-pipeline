#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

print("Folder structure ready.")


# In[2]:


import requests
import pandas as pd
from datetime import date
import os

URL = "https://remoteok.com/api"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=HEADERS)
response.raise_for_status()

data = response.json()

# First item is metadata — remove it
jobs = data[1:]

records = []

for job in jobs:
    records.append({
        "job_id": job.get("id"),
        "job_title": job.get("position"),
        "company": job.get("company"),
        "location": job.get("location"),
        "salary": job.get("salary"),
        "tags": ", ".join(job.get("tags", [])),
        "job_url": job.get("url"),
        "date_scraped": date.today().isoformat()
    })

df = pd.DataFrame(records)

# Ensure folder exists
os.makedirs("data/raw", exist_ok=True)

file_name = f"data/raw/remoteok_{date.today().isoformat()}.csv"
df.to_csv(file_name, index=False)

print(f"✅ Saved {len(df)} jobs to {file_name}")


# In[3]:


import pandas as pd
import glob
import os

raw_files = glob.glob("data/raw/*.csv")

if not raw_files:
    raise Exception("No raw CSV files found.")

df_list = [pd.read_csv(file) for file in raw_files]

master_df = pd.concat(df_list, ignore_index=True)

# Drop duplicate job_id + date combinations
master_df.drop_duplicates(
    subset=["job_id", "date_scraped"],
    inplace=True
)

os.makedirs("data/processed", exist_ok=True)

master_path = "data/processed/remoteok_master.csv"
master_df.to_csv(master_path, index=False)

print(f"✅ Master dataset updated with {len(master_df)} rows")


# In[4]:


import os
os.getcwd()


# In[5]:


os.listdir()


# In[1]:


import os
os.getcwd()


# In[2]:


os.listdir()


# In[3]:


import os

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

os.listdir()


# In[4]:


os.listdir("data")


# In[ ]:




