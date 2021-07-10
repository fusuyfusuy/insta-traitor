import io
from bs4 import BeautifulSoup
followersFile = open("followers.html", "r")
followingFile = open("following.html", "r")
followers = BeautifulSoup(followersFile, 'html.parser')
following = BeautifulSoup(followingFile, 'html.parser')

fsAr = []
fsList = followers.findAll("a")
for child in fsList:
    if ( child.get_text().strip() != "" ):
        fsAr.append(child.get_text().strip())

fwAr = []
fwList = following.findAll("a")
for child in fwList:
    if ( child.get_text().strip() != "" and child.get_text().strip() != "undefinedundefined" and child.get_text().strip() != "People" and child.get_text().strip() != "Hashtags"):
        fwAr.append(child.get_text().strip())

traited = set(fsAr) - set(fwAr)
traitors = set(fwAr) - set(fsAr)

counter = 1

print ("Takip etmediklerim:")
for i in traited:
    print (counter,":   ", i)
    counter += 1

print ("\n")
counter = 1
print ("Takip etmeyenler:")
for i in traitors:
    print (counter,":   ", i)
    counter += 1
