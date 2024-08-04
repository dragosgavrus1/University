% predicate to determine all possibilities of colouring n countries with m colours
colour_map(N, M, Map) :-
    length(Map, N), % Create a list of length N
    valid_map(Map, M), 
    adjacent_countries(Map).

% predicate to check if the map is valid
valid_map([], _).
valid_map([Color|Rest], M) :-
    between(1, M, Color), % color should be between 1 and M
    valid_map(Rest, M).

% predicate to check if adjacent countries have the same colour
adjacent_countries([_]).
adjacent_countries([C1, C2 | Rest]) :-
    C1 \= C2, 
    adjacent_countries([C2 | Rest]). 


all_color_maps(N, M, Maps) :-
    findall(Map, colour_map(N, M, Map), Maps).
% all_color_maps(3, 2, Maps).
