# 2020-7-2 17:37:34

print("\nProcessing tags......")

# load the Tags file
TagsRawFile='Tags_raw'
FileHandle=open(TagsRawFile, 'r', encoding='UTF-8')
sTag=FileHandle.read()
FileHandle.close()

# split the string by a comma (in Chinese)
sTag=sTag.split('，')

# remove duplicates
sTag=sTag[0:len(sTag)] # neglect the first one
N0=len(sTag)
sTag=list(set(sTag))
sTag.sort()
if sTag[0]=='':
    sTag=sTag[1:len(sTag)] # neglect the blank
N1=len(sTag)
N2=N0-N1
print("The number of tags: {}".format(N0))
print("The number of duplicated tags: {}".format(N2))
print("The number of remaining tags: {}".format(N1))

# write the Tags file
TagsUniqueFile='Tags_unique'
FileHandle=open(TagsUniqueFile,'w',encoding='UTF-8')
FileHandle.close()
nTag=len(sTag)
iTag=0
for cTag in sTag:
    FileHandle=open(TagsUniqueFile, 'a', encoding='UTF-8')
    FileHandle.write(cTag)
    if iTag!=nTag-1:
        FileHandle.write("，")
    FileHandle.close()
    iTag=iTag+1