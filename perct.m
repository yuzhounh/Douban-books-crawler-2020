function perct(t,i,n,k)
%PERCT The program procedure.
% PERCT(T,I,N,K) shows the program procedure and remaining time for loops.
% Only K countdowns will be displayed. When the program is completed,
% output the total elapsed time with scale .0000 hours.
%
% t, time elapsed (seconds) recorded by "tic" and "toc"
% i, the number of loops that are completed
% n, the total number of loops
% k, the number of countdowns to be dispalyed, optional
%
% Example:
%     k=10;
%     tic;
%     for i=1:n
%         ...
%         perct(toc,i,n,k);
%     end
%
% Tips:
% 1, you might save the elapsed time by "time=toc/3600" after all loops
%   are completed.
% 2, "clc" before calling this function if you only want to see the current
%   countdown.

% Jing Wang
% 2020-7-3

% If k exists, output k countdowns; else, output n countdowns.
if nargin==3 || ( nargin==4 && ismember(i,ceil(n*[1:k]/k)) )
    % percentage
    fprintf('The program has run: %0.1f%%.\n', i*100/n);
    
    t=t/60; 
    tm=t*(n-i)/i; 
    if tm~=0
        fprintf('Remaining time: %0.1f minutes.', tm);
    else
        fprintf('Elapsed time: %0.1f minutes.',t);
    end
    
    fprintf('\n\n');
end