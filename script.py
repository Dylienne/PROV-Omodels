#written by Dylienne Every 2127946
#Department of Computer Sciences VU AMSTERDAM
#Master Thesis

import json
import ijson
import pandas as pd
import numpy as np
import prov

#definition of contents
document = pd.read_json('Data/KOAPROV.json')
# print(document)
Bundles = document["bundle"]
provenance = Bundles["result:provenance"]
elementoverview = list(provenance)

#pandas dataframe
df = pd.DataFrame(provenance)
print(df.count())

#timestamp extraction

# def time_info():
#     generated= df['wasGeneratedBy']

# for line in df['wasStartedBy']:
#     timelines = []
#     if line == '_start':
#         timelines.append(line)
#     print(timelines)
#

