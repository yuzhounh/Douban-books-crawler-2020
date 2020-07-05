% integrate the results from doulists and tags
% 2017-1-21 22:04:32

clear;

fprintf('Sort all books......\n');

% from doulists
load Books_doulists;
ID_0=ID;
rating_0=rating;
votes_0=votes;
title_0=title;

% from tags
% do not record the translator
load Books_tags;
ID=[ID_0;ID];
rating=[rating_0;rating];
votes=[votes_0;votes];
title=[title_0;title];

% remove duplicates
[ID,ix,~]=unique(ID);
rating=rating(ix);
votes=votes(ix);
title=title(ix);

% save all books
save('Books.mat','ID','rating','votes','title');

% score
delta=2.5;
threshold=(9.0-delta)*log(1000); % 44.90
score=(rating-delta).*log(votes); 
score(isinf(score))=0;

% sort by score
[score,ix]=sort(score,'descend');
ID=ID(ix);
rating=rating(ix);
votes=votes(ix);
title=title(ix);

% books with rating and votes higher than a threshold
sTh=[0.0, 0; 9.0, 1000; 8.5, 0];
[nTh,~]=size(sTh);
for iTh=1:nTh
    ixTh=rating>=sTh(iTh,1) & votes>=sTh(iTh,2);
    
    ID_sbt=ID(ixTh); % subset
    rating_sbt=rating(ixTh);
    votes_sbt=votes(ixTh);
    title_sbt=title(ixTh);

    fileID=fopen(sprintf('Books_%d',iTh),'w');
    fprintf(fileID,sprintf('%s\n\n',datestr(datetime,'yyyy-mm-dd HH:MM:SS')));
    fprintf(fileID,sprintf('Books with rating >= %0.1f and votes >= %d. \n', sTh(iTh,1), sTh(iTh,2)));
    fprintf(fileID,sprintf('Total number: %d \n\n', length(ID_sbt)));
    fprintf(fileID,'ID, rating, votes, title\n');
    nBook=length(ID_sbt);
    for iBook=1:nBook
        fprintf(fileID,'%08d, %0.1f, %d, %s\n', ID_sbt(iBook), rating_sbt(iBook), votes_sbt(iBook), title_sbt{iBook,1});
    end
    fclose(fileID);
end
fprintf('\n');