% 2020-7-2 12:29:53

clear;

fileID=fopen('Doulists_name','w','n','UTF-8');

sDoulist=dir('Doulists');
sDoulist=sDoulist(3:end);

nDoulist=length(sDoulist);
for iDoulist=1:nDoulist
    cDoulist=sDoulist(iDoulist).name;
    fprintf(fileID,sprintf('%s\n', cDoulist));  
    
    cDoulist=string(cDoulist);
    tmp(iDoulist,1)=cDoulist;
end

sDoulist=tmp;
nDoulist=length(sDoulist);
save('Doulists_name.mat','sDoulist','nDoulist');