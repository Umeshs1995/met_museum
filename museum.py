import pandas
import numpy
import csv
import json

import pandas as pd
import requests
from flatten_json import flatten

urls = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

response = requests.get(urls)
my_json = response.json()

object_id = my_json['objectIDs'][:20]

lst=[]
for x in object_id:
    Urls="https://collectionapi.metmuseum.org/public/collection/v1/objects"+'/'+f"{str(x)}"
    resp=requests.get(Urls)
    my_json=resp.json()

    flatten_data=flatten(my_json)

    df=pd.DataFrame.from_dict(flatten_data,orient='index')
    lst.append(df)

data=pd.concat(lst,axis=1)
data1=data.transpose()
data1.to_csv('museum.csv',index=False,encoding='utf-8-sig',)
print('done')
