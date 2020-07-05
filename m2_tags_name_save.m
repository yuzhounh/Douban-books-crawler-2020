% 2020-7-2 12:29:53

clear;

fileID=fopen('Tags_name','w','n','UTF-8');

sTag=dir('Tags');
sTag=sTag(3:end);

nTag=length(sTag);
for iTag=1:nTag
    cTag=sTag(iTag).name;
    fprintf(fileID,sprintf('%s\n', cTag));  
    
    cTag=string(cTag);
    tmp(iTag,1)=cTag;
end

sTag=tmp;
nTag=length(sTag);
save('Tags_name.mat','sTag','nTag');