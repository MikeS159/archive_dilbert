from glob import glob
import pandas as pd
import numpy as np
import json

glob("*/*.gif", recursive=True)
filenames = [i.split("/")[1].replace(".gif", "") for i in glob("*/*.gif", recursive=True)]
dates = [i.split("_")[0] for i in filenames]
tags = [i.split("_")[1:] for i in filenames]
alltags = [tag for taglist in tags for tag in taglist]

alltags = pd.DataFrame(alltags).drop_duplicates(ignore_index=True)
alltags = alltags[0].to_list()
index = [(z, [dates[i] for i, y in enumerate(tags) if z in y]) for j, z in enumerate(alltags)]
my_dict = dict(index)

with open('index.json', 'w') as index_file:
    json.dump(my_dict, index_file)
