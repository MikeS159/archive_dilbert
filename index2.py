from glob import glob
import pandas as pd
import numpy as np
import json
from PIL import Image
import pyocr

glob("*/*.gif", recursive=True)
filenames = [i.split("/")[1].replace(".gif", "") for i in glob("*/*.gif", recursive=True)]
dates = [i.split("_")[0] for i in filenames]

texts = []
for file in filenames:
    my_img = Image.open(file.split("-")[0] + "/"+ file+".gif")
    my_img = my_img.convert('RGB')
    my_tool = [tool for tool in pyocr.get_available_tools() if tool.__spec__.name=="pyocr.tesseract"][0]
    my_text = my_tool.image_to_string(my_img, lang="eng", builder=pyocr.builders.TextBuilder()).replace("\n"," ").replace("- ", " ")
    my_text = my_text.replace("Scott Adams, Inc. /Dist.","").replace("Dilbert.com _DilbertCartoonist@gmail.com", "")
    texts.append(my_text)

words = [i.split(" ") for i in texts]

words = pd.DataFrame(words).drop_duplicates(ignore_index=True)
words = words[0].to_list()
index = [(z, [dates[i] for i, y in enumerate(texts) if z in y]) for j, z in enumerate(words)]
my_dict = dict(index)

with open('index2.json', 'w') as index_file:
    json.dump(my_dict, index_file)
