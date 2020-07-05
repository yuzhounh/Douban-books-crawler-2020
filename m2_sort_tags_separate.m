% 2017-1-10 16:25:54

clear;

fprintf('Sort books for each tag......\n\n');

% create a folder the save the sorted results
dirname='Tags_sort';
if ~exist(dirname,'dir')
    mkdir(dirname);
end

% record the number of books in each tag
fileID_info=fopen('Tags_info','w');
fprintf(fileID_info,sprintf('%s\n\n',datestr(datetime,'yyyy-mm-dd HH:MM:SS')));

load Tags_name_print.mat;
sTag_print=sTag;

load Tags_name.mat;
nTag=length(sTag);

fprintf(fileID_info,sprintf('The number of tags: %d\n\n',nTag));
fprintf(fileID_info,'number of books, tag\n');

tic;
for iTag=1:nTag    
    % import books from each tags
    cTag=sTag(iTag,1);
    cTag_print=sTag_print(iTag,1);
    load(sprintf('Tags_mat/%s.mat',cTag));
    
    % remove duplicates
    [ID,ix,~]=unique(ID);
    rating=rating(ix);
    votes=votes(ix);
    title=title(ix);
    
    nBook=length(ID);
    fprintf(fileID_info,sprintf('%03d, %s\n',nBook,cTag_print));
    
    % score
    delta=2.5;
    score=(rating-delta).*log(votes);
    score(isinf(score))=0;
    
    % sort by score
    [~,ix]=sort(score,'descend');
    ID=ID(ix);
    rating=rating(ix);
    votes=votes(ix);
    title=title(ix);
    
    % export sorted books for each tag
    exportfilename=sprintf('%s/%s',dirname,cTag);
    fileID=fopen(exportfilename,'w');
    fprintf(fileID,sprintf('%s\n\n',datestr(datetime,'yyyy-mm-dd HH:MM:SS')));
    fprintf(fileID,'number of books, tag name\n');
    fprintf(fileID,sprintf('%d, %s\n\n',nBook,cTag_print));
    fprintf(fileID,'ID, rating, votes, title\n');
    for iBook=1:nBook
        fprintf(fileID,'%08d, %0.1f, %d, %s\n', ID(iBook), rating(iBook), votes(iBook), title{iBook,1});
    end
    fclose(fileID);
    
    perct(toc,iTag,nTag,30);
end
fclose(fileID_info);
fprintf('\n');