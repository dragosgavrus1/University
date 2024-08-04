% Problema: Define predicate that removes the first 3 occurences of a given element from a list.
% If the element has less than 3 occurences all the occurences will be removed
% Ex: [1,2,3,4,5,2], 2 becomes 1,3,4,5 


% remove_first_3_occurrences(E - element, L - list, R - result)
remove_first_3_occurrences(_, [], []).
remove_first_3_occurrences(X, [X|T], Result) :-
    remove_first_3_occurrences(X, T, Result).
remove_first_3_occurrences(X, [H|T], [H|Result]) :-
    X \= H,
    remove_first_3_occurrences(X, T, Result).

