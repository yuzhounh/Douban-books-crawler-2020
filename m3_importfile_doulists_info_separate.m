%% Import data from text file.
% Script for importing data from the following text file:
%
%    E:\Python\20170107 Douban Books\Douban_10_doulist\Doulist\Doulist_45709528
%
% To extend the code to different selected data or a different text file,
% generate a function instead of a script.

% Auto-generated by MATLAB on 2020/07/02 16:44:06

clear;

% create a folder to store the .mat files
dirname='Doulists_info_mat';
if ~exist(dirname,'dir')
    mkdir(dirname);
end

load Doulists_name.mat;

for iDoulist=1:nDoulist
    % current doulist name
    cDoulist=sDoulist(iDoulist);
    
    %% Initialize variables.
    filename = sprintf('Doulists/%s',cDoulist);
    delimiter = ',';
    startRow = 2;
    endRow = 2;
    
    %% Format for each line of text:
    %   column1: double (%f)
    %	column2: double (%f)
    %   column3: text (%s)
    % For more information, see the TEXTSCAN documentation.
    formatSpec = '%f%f%s%*s%*s%*s%*s%*s%*s%*s%*s%[^\n\r]';
    
    %% Open the text file.
    fileID = fopen(filename,'r');
    
    %% Read columns of data according to the format.
    % This call is based on the structure of the file used to generate this
    % code. If an error occurs for a different file, try regenerating the code
    % from the Import Tool.
    textscan(fileID, '%[^\n\r]', startRow-1, 'WhiteSpace', '', 'ReturnOnError', false);
    dataArray = textscan(fileID, formatSpec, endRow-startRow+1, 'Delimiter', delimiter, 'TextType', 'string', 'ReturnOnError', false, 'EndOfLine', '\r\n');
    
    %% Close the text file.
    fclose(fileID);
    
    %% Post processing for unimportable data.
    % No unimportable data rules were applied during the import, so no post
    % processing code is included. To generate code which works for
    % unimportable data, select unimportable cells in a file and regenerate the
    % script.
    
    %% Allocate imported array to column variable names
    doulist_ID = dataArray{:, 1};
    number_of_books = dataArray{:, 2};
    doulist_title = dataArray{:, 3};
    
    
    %% Clear temporary variables
    clearvars filename delimiter startRow endRow formatSpec fileID dataArray ans;
    
    %% save the results
    save(sprintf('Doulists_info_mat/%s.mat',cDoulist),'doulist_ID','number_of_books','doulist_title');
end