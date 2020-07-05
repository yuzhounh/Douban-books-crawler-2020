% main script
% 2020-7-2 14:28:14

clear,clc;

% % douban crawler
% system('python main.py')

% sort all books
m1_importfile_doulists;
m1_importfile_tags;
m1_sort;

% sort books for each tag
m2_tags_name_save;
m2_tags_name_print;
m2_importfile_tags_separate;
m2_sort_tags_separate;

% sort books for each doulist
m3_doulists_name_save;
m3_importfile_doulists_info_separate;
m3_importfile_doulists_separate;
m3_sort_doulists_separate;