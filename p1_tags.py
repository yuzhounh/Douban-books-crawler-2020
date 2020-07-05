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

# open the url and read
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
def getHtml(url):
    url_new=quote(url,safe=string.printable)
    req=urllib.request.Request(url=url_new, headers=headers)
    page=urllib.request.urlopen(req)
    html=page.read().decode('UTF-8')
    page.close()
    return html

def getBookInfo(html):
    temp=r'<a href="https://book.douban.com/subject/(.*)/" title="(.*)" \n  (.*)>\n\n    (.*)\n\n\n    \n      <span style="font-size:12px;"> : (.*) </span>\n\n  </a>\n\n      </h2>\n      <div class="pub">\n        \n  \n  (.*)\n\n      </div>\n\n\n        \n  \n  \n  \n  <div class="star clearfix">\n        <span class="allstar(.*)"></span>\n        <span class="rating_nums">(.*)</span>\n\n    <span class="pl">\n        (.*)人评价(.*)\n    </span>\n  </div>'
    temp=re.compile(temp)
    temp=re.findall(temp, html)
    temp_0=temp

    temp=r'<a href="https://book.douban.com/subject/(.*)/" title="(.*)" \n  (.*)>\n\n    (.*)\n\n\n    \n\n  </a>\n\n      </h2>\n      <div class="pub">\n        \n  \n  (.*)\n\n      </div>\n\n\n        \n  \n  \n  \n  <div class="star clearfix">\n        <span class="allstar(.*)"></span>\n        <span class="rating_nums">(.*)</span>\n\n    <span class="pl">\n        (.*)人评价(.*)\n    </span>\n  </div>'
    temp=re.compile(temp)
    temp=re.findall(temp, html)
    temp_1=temp

    temp_0.extend(temp_1)
    return temp_0
    
# most of the results are stored in this file    
ResultFile='Books_tags'
FileHandle=open(ResultFile,'w')
FileHandle.write("ID, rating, votes, title, author, (translator), publisher, date, price\n")
FileHandle.close()

# make a directory to store the results for each Tags separately
TagsDir='Tags'
if not os.path.exists(TagsDir):
    os.mkdir(TagsDir)

# import the Tags ID from a text file
TagsFile='Tags_unique'
FileHandle=open(TagsFile,'r',encoding='UTF-8')
sTag=FileHandle.read()  # set of tags
FileHandle.close()
sTag=sTag.split('，')

# some special cases for checking the codes
# sTag=['历史','文学']

nTag=len(sTag)
iTag=0
for cTag in sTag:  # current tag
    iTag=iTag+1
    print("\nProcessing Tags {} of {}.\nTag: {}".format(iTag, nTag, cTag))
    
    PageNumber=50   # grab 50 pages, a tuning parameter
    BooksPerPage=20  # 20 books in each page
    BookNumber=BooksPerPage*PageNumber 
   
    TagsFile="Tags/{}".format(cTag)
    FileHandle=open(TagsFile,'w',encoding='UTF-8')
    FileHandle.write("Tag: {} \n\n".format(cTag))
    FileHandle.write("ID, rating, votes, title, author, (translator), publisher, date, price\n")
    FileHandle.close()
    
    # crawl the pages in a Tags
    for i in range(0,PageNumber):
        print("Page {}".format(i+1))
        
        url='https://book.douban.com/tag/{}?start={}'.format(cTag, i*BooksPerPage)
        try:
            html = getHtml(url)
        except:  # for broken links
            break

        BookInfo=getBookInfo(html)
        
        if len(BookInfo)==0:
            break
        
        LenBook=BooksPerPage
        if len(BookInfo)!=BooksPerPage:
            LenBook=len(BookInfo) # update the number of books
        
        for j in range(0,LenBook):
            tmp=BookInfo[j]
            
            # book information
            if len(tmp)==9:
                ID=tmp[0]
                title=tmp[1]
                rating=tmp[6]
                votes=tmp[7]
                others=tmp[4]
            elif len(tmp)==10:
                ID=tmp[0]
                title=tmp[1]
                rating=tmp[7]
                votes=tmp[8]
                others=tmp[5]
            
            if rating=='':
                rating='0.0'
            votes=votes[1:len(votes)]
            others=others.replace(' /',',')
            
            ID=int(ID)
            votes=int(votes)
            
            FileHandle=open(ResultFile,'a',encoding='UTF-8')
            FileHandle.write("{:0>8d}, {}, {:0>6d}, {}, {}\n".format(ID, rating, votes, title, others))
            FileHandle.close()
            
            FileHandle=open(TagsFile,'a',encoding='UTF-8')
            FileHandle.write("{:0>8d}, {}, {:0>6d}, {}, {}\n".format(ID, rating, votes, title, others))
            FileHandle.close()
