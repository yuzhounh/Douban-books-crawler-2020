# 2020-7-2 17:37:34

import re
import string
import urllib
import time
import random
import urllib.request
from urllib.parse import quote

# Note
# https://www.douban.com/note/x
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
def getHtml(url):
    url_new=quote(url,safe=string.printable)
    req=urllib.request.Request(url=url_new, headers=headers)
    page=urllib.request.urlopen(req)
    html = page.read().decode('UTF-8')
    page.close()
    return html
    
# Doulist
# https://www.douban.com/doulist/x
def getList(html):
    tmp=r'<a class="link" href="https://www.douban.com/doulist/(\d*)/" rel="nofollow">https://www.douban.com/doulist/'
    tmp=re.compile(tmp)
    tmp=re.findall(tmp,html)
    return tmp

print("\nProcessing notes......")

# import the note ID 
NoteFile='Notes'
FileHandle=open(NoteFile,'r')
sNote=FileHandle.read()
FileHandle.close()

sNote=sNote.split(', ')  # sets of notes
nNote=len(sNote)  # number of notes

# output the doulists
DoulistFile='Doulists_ID'
FileHandle=open(DoulistFile,'w')
FileHandle.close()

# read the notes and output the doulist IDs in the notes
iNote=0
for cNote in sNote:  # current note    
    UrlNote="https://www.douban.com/note/{}".format(cNote)
    html=getHtml(UrlNote)
    sDoulist=getList(html)
    nDoulist=len(sDoulist)
    for iDoulist in range(nDoulist):
        FileHandle=open(DoulistFile,'a')
        FileHandle.write("{}".format(sDoulist[iDoulist]))
        if (iNote!=nNote-1 or iDoulist!=nDoulist-1):
            FileHandle.write(", ")
        FileHandle.close()

    iNote = iNote + 1

# read the doulist file
FileHandle=open(DoulistFile,'r',encoding='UTF-8')
sDoulist=FileHandle.read()  # set of lists
FileHandle.close()

# split the string by a comma
sDoulist=sDoulist.split(', ')

# str to int
tmp=sDoulist
count=0
for cDoulist in sDoulist:
    tmp[count]=int(cDoulist)
    count=count+1
sDoulist=tmp    

# remove duplicates
N0=len(sDoulist)
sDoulist=list(set(sDoulist))
sDoulist.sort()
N1=len(sDoulist)
N2=N0-N1
print("The number of notes: {}".format(nNote))
print("The number of doulists: {}".format(N0))
print("The number of duplicated doulists: {}".format(N2))
print("The number of remaining doulists: {}".format(N1))

# rewrite the doulist file
nDoulist=len(sDoulist)
FileHandle=open(DoulistFile,'w',encoding='UTF-8')
FileHandle.close()
for iDoulist in range(nDoulist):
    FileHandle=open(DoulistFile,'a')
    FileHandle.write("{}".format(sDoulist[iDoulist]))
    if iDoulist!=nDoulist-1:
        FileHandle.write(", ")
    FileHandle.close()
