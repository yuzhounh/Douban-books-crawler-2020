% 2017-1-10 16:25:54

clear;

fprintf('Sort books for each doulist......\n\n');

% create a folder the save the sorted results
dirname='Doulists_sort';
if ~exist(dirname,'dir')
    mkdir(dirname);
end

% record the number of books in each Doulist
fileID_info=fopen('Doulists_info','w');
fprintf(fileID_info,sprintf('%s\n\n',datestr(datetime,'yyyy-mm-dd HH:MM:SS')));

load Doulists_name.mat;
nDoulist=length(sDoulist);

fprintf(fileID_info,sprintf('The number of Doulists: %d\n\n',nDoulist));
fprintf(fileID_info,'doulist ID, number of books, doulist name\n');

tic;
for iDoulist=1:nDoulist
    % import books from each Doulists
    cDoulist=sDoulist(iDoulist,1);
    load(sprintf('Doulists_mat/%s.mat',cDoulist));
    load(sprintf('Doulists_info_mat/%s.mat',cDoulist));
    
    % remove duplicates
    [ID,ix,~]=unique(ID);
    rating=rating(ix);
    votes=votes(ix);
    title=title(ix);
    
    nBook=length(ID);
    fprintf(fileID_info,sprintf('%08d, %04d, %s\n',doulist_ID,number_of_books,doulist_title));
    
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
    
    % export sorted books for each Doulist
    exportfilename=sprintf('%s/%s',dirname,cDoulist);
    fileID=fopen(exportfilename,'w');
    fprintf(fileID,sprintf('%s\n\n',datestr(datetime,'yyyy-mm-dd HH:MM:SS')));
    fprintf(fileID,'doulist ID, number of books, doulist name\n');
    fprintf(fileID,sprintf('%08d, %04d, %s\n\n',doulist_ID,number_of_books,doulist_title));
    fprintf(fileID,'ID, rating, votes, title\n');
    for iBook=1:nBook
        fprintf(fileID,'%08d, %0.1f, %d, %s\n', ID(iBook), rating(iBook), votes(iBook), title{iBook,1});
    end
    fclose(fileID);
    
    perct(toc,iDoulist,nDoulist,30);
end
fclose(fileID_info);
fprintf('\n');