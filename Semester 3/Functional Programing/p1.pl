substitute(_, _, [], []).
% if the element X is found at the head of the input list, replace it with Y 
substitute(X, Y, [X|T], [Y|T2]) :-
    substitute(X, Y, T, T2).
substitute(X, Y, [H|T], [H|T2]) :-
    H \= X,
    substitute(X, Y, T, T2).
% substitute(3, 4, [1, 2, 3, 4, 3, 5], Result).


sublist([X|_], 1, 1, [X]).
% skip elements
sublist([_|T], M, N, Sublist) :-
    M > 1,
    M1 is M - 1,
    N1 is N - 1,
    sublist(T, M1, N1, Sublist).
% start building the sublist 
sublist([X|T], 1, N, [X|Sublist]) :-
    N > 1,
    N1 is N - 1,
    sublist(T, 1, N1, Sublist).
% sublist([1, 2, 3, 4, 5, 6, 7], 3, 5, Sublist).