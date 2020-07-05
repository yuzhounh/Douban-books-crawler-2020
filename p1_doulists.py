# 2020-7-2 17:37:34

import re
import string
import urllib
import math
import time
import random
import os
import urllib.request
from urllib.parse import quote

# constant
delta=2.5 
threshold=(9.0-delta)*math.log(1000) # the threshold of a good book
BookPerPage=25 # the number of books per page (except for the last one)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
def getHtml(url):
    url_new=quote(url,safe=string.printable)
    req=urllib.request.Request(url=url_new, headers=headers)
    page=urllib.request.urlopen(req)
    html = page.read().decode('UTF-8')
    page.close()
    return html
    
def getDoulistTitle(html):
    tmp=r'<title>(.*)</title>'
    tmp=re.compile(tmp)
    tmp=re.findall(tmp,html)
    tmp=tmp[0]
    return tmp

def getBookNumber(html):
    # tmp=r'"active">\xe5\x85\xa8\xe9\x83\xa8<span>(.*)</span></a>'
    tmp=r'class="active">全部<span>(.*)</span></a>'
    tmp=re.compile(tmp)
    tmp=re.findall(tmp,html)
    if tmp==[]:
        tmp=0
    else:
        tmp=tmp[0]
        tmp=int(tmp[1:-1])
    return tmp

def getBookInfo(html):
    tmp=r'<a href="https://book.douban.com/subject/(.*)/" target="_blank">\n        (.*)\n      </a>\n    </div>\n    \n      <div class="rating">\n          <span class="allstar(.*)"></span>\n          <span class="rating_nums">(.*)</span>\n          <span>(.*)</span>\n      </div>\n    <div class="abstract">\n      \n          作者: (.*)\n            <br />\n          出版社: (.*)\n            <br />\n          出版年: (.*)\n    </div>'
    tmp=re.compile(tmp)
    tmp=re.findall(tmp,html)
    return tmp
    
# most of the results are stored in this file    
ResultFile='Books_doulists'
FileHandle=open(ResultFile,'w',encoding='UTF-8')
FileHandle.write("ID, rating, votes, date, title, author, publisher\n")
FileHandle.close()

# record the number of books in each doulist
DoulistInfoFile='Doulists_info'
FileHandle=open(DoulistInfoFile,'w',encoding='UTF-8')
FileHandle.write("doulist, number of books, title\n")
FileHandle.close()

# make a directory to store the results for each doulist separately
DoulistDir='Doulists'
if not os.path.exists(DoulistDir):
    os.mkdir(DoulistDir)

# import the doulist ID from a TXT file
FileHandle=open('Doulists_ID','r',encoding='UTF-8')
sDoulist=FileHandle.read()
FileHandle.close()
sDoulist=sDoulist.split(', ')
tmp=sDoulist
count=0
for cDoulist in sDoulist:
    tmp[count]=int(cDoulist) # str to int
    count=count+1
sDoulist=tmp
nDoulist=len(sDoulist)

# some special cases for checking the codes
# sDoulist=[4031665, 176014, 133120, 1739529, 821278, 1197610]
# sDoulist=[1197610]
# sDoulist=[10187]
sDoulist=[49176211]

iDoulist=0
for cDoulist in sDoulist:
    iDoulist=iDoulist+1
    print("\nProcessing doulist {} of {}.\nDoulist ID: {}".format(iDoulist, nDoulist, cDoulist))

    # https://www.douban.com/doulist/x
    # to get the number of books in a doulist
    url="https://www.douban.com/doulist/{}".format(cDoulist)
    try:
        html=getHtml(url)
    except: # for broken links
        continue

    DoulistTitle=getDoulistTitle(html)
    BookNumber=getBookNumber(html)
    
    # Number of Books
    FileHandle=open(DoulistInfoFile,'a',encoding='UTF-8')
    FileHandle.write("{:0>8d}, {:0>5d}, {}\n".format(cDoulist, BookNumber, DoulistTitle))
    FileHandle.close()
   
    DoulistFile='Doulists\Doulist_{:0>8d}'.format(cDoulist)
    FileHandle=open(DoulistFile,'w',encoding='UTF-8')
    FileHandle.write("doulist, number of books, title\n")
    FileHandle.write("{:0>8d}, {:0>3d}, {}\n\n".format(cDoulist, BookNumber, DoulistTitle))
    FileHandle.write("ID, rating, votes, date, title, author, publisher\n")
    FileHandle.close()    
    
    # crawl the pages in a doulist
    for i in range(0,int(BookNumber/BookPerPage+1)):
        print("Page {} of {}".format(i+1, int(BookNumber/BookPerPage+1)))

        # the expected number of books in the current page
        if i<int(BookNumber/BookPerPage):
            LenBook=BookPerPage
        else:
            LenBook=BookNumber-int(BookNumber/BookPerPage)*BookPerPage
        
        tmp=i*BookPerPage
        url="https://www.douban.com/doulist/{}/?start={}".format(cDoulist,tmp)
        html=getHtml(url)
        BookInfo=getBookInfo(html)
        
        if len(BookInfo)!=LenBook:
            LenBook=len(BookInfo) # update the number of books
        
        for j in range(0,LenBook):
            tmp=BookInfo[j]
            
            # seven kinds of information
            ID=tmp[0]
            title=tmp[1]
            rating=tmp[3]
            votes=tmp[4]
            author=tmp[5]
            publisher=tmp[6]
            date=tmp[7]

            ID = int(ID)
            if rating=='':
                rating='0.0'
            votes=int(votes[1:-4])
            
            FileHandle=open(ResultFile,'a',encoding='UTF-8')
            FileHandle.write("{:0>8d}, {}, {:0>6d}, {}, {}, {}, {}\n".format(ID, rating, votes, date, title, author, publisher))
            FileHandle.close()
            
            FileHandle=open(DoulistFile,'a',encoding='UTF-8')
            FileHandle.write("{:0>8d}, {}, {:0>6d}, {}, {}, {}, {}\n".format(ID, rating, votes, date, title, author, publisher))
            FileHandle.close()
