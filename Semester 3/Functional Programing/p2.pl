% a
substitute(_, _, [], []).

% if the element X is found at the head of the input list, replace it with Y 
substitute(X, Y, [X|T], [Y|T2]) :-
    substitute(X, Y, T, T2).

substitute(X, Y, [H|T], [H|T2]) :-
    H \= X,
    substitute(X, Y, T, T2).
% substitute(3, 7, [1, 2, 3, 4, 3, 5], Result).

% b
% count occurrences of an element in a list
count_occurrences(_, [], 0).
count_occurrences(X, [X|T], N) :-
    count_occurrences(X, T, N1),
    N is N1 + 1.
count_occurrences(X, [Y|T], N) :-
    X \= Y,
    count_occurrences(X, T, N).

% find the maximum element in a list
max_list([X], X).
max_list([H|T], Max) :-
    max_list(T, MaxT),
    Max is max(H, MaxT).

% replace all occurrences of an element in a list
replace(_, _, [], []).
replace(Old, New, [Old|T], [New|T1]) :-
    replace(Old, New, T, T1).
replace(Old, New, [H|T], [H|T1]) :-
    Old \= H,
    replace(Old, New, T, T1).

% find the most frequent number in a list
most_frequent_number(List, MostFrequentNumber) :-
    most_frequent_number_helper(List, _, 0, MostFrequentNumber).

most_frequent_number_helper([], MostFrequentNumber, _, MostFrequentNumber).
most_frequent_number_helper([H|T], CurrentNumber, CurrentCount, MostFrequentNumber) :-
    count_occurrences(H, T, Occurrences),
    (Occurrences > CurrentCount ->
        most_frequent_number_helper(T, H, Occurrences, MostFrequentNumber)
    ;
        most_frequent_number_helper(T, CurrentNumber, CurrentCount, MostFrequentNumber)
    ).

replace_in_sublists([], _, []).
replace_in_sublists([H|T], MostFrequentNumber, [NewH|NewT]) :-
    (is_list(H) ->
        max_list(H, MaxInSublist),
        replace(MostFrequentNumber, MaxInSublist, H, UpdatedSublist),
        NewH = UpdatedSublist,
        replace_in_sublists(T, MostFrequentNumber, NewT)
    ;
        NewH = H,
        replace_in_sublists(T, MostFrequentNumber, NewT)
    ).

% find the most frequent number and replace occurrences in sublists
find_and_replace_most_frequent(List, Result) :-
    most_frequent_number(List, MostFrequentNumber),
    replace_in_sublists(List, MostFrequentNumber, Result).
% find_and_replace_most_frequent([1, [2, 5, 7], 4, 5, [1, 4], 3, [1, 3, 5, 8, 5, 4], 5, [5, 9, 1], 2], Result).