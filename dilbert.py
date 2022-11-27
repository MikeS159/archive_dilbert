#requests was broken on my server for some reason, so there is a workaround
#import requests
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urljoin
from datetime import date, timedelta

startUrl = "https://dilbert.com/strip/"
currentDate = date(1989, 4, 16) #Starting date (first Dilbert)
#You neeed folders created for this to work, use command below on Linux to make them
#mkdir -p {1989..2022}
year = currentDate.year #Keep track of year so we can put images in sub-folders

while(currentDate != date.today()) : #Loop until todays date is reached
    try : #Dirty way of hadling connection errors etc
        #uncoment if using requests and remove the next 4 lines after
        #result = requests.get(startUrl + str(currentDate))
        fp = urllib.request.urlopen(startUrl + str(currentDate))
        bytes = fp.read()
        result = bytes.decode("utf8")
        fp.close()

        #doc = BeautifulSoup(result.text, "html.parser")
        doc = BeautifulSoup(result, "html.parser")  #remove if using requests
        comImg = doc.find_all("img", {"class" : "img-responsive img-comic"}) #The comic strip is in a image tag with a unique class name
        getUrl = comImg[0]["src"] #grab the actual URL for the image from the CDN

        tagList = []
        tagsPara = doc.find_all("p", {"class" : "small comic-tags"}) #Get the paragraph with the tag links in
        tagsLink = tagsPara[0].find_all("a") #Get the tag lines
        for name in tagsLink :
            tagList.append(''.join(name.findAll(text=True))) #Strip out the actual tag names

        searchName = ""
        for tag in tagList :
            searchName += "_" + tag #Build string of tag names for filename
        searchName = searchName.replace("/", "-") #Remove any / since it messes up the files names

        urllib.request.urlretrieve(getUrl, str(year) + "/" + str(currentDate) + searchName + ".gif") #Get the image from the URL add date and tags as file name, put in year folder
        currentDate = currentDate + timedelta(days=1) #Next day
        year = currentDate.year #Update current year
    except:
        print("Error on " + str(currentDate) + " re-trying") #Keep track of errors, if the same error keeps happening there is some edge case/page difference that needs handling seperatly
