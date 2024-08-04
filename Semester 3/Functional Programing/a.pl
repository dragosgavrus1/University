
% minim([A], A).
% minim([H|T], M):-
%     minim(T, M),
%     H > M,
%     !.
% minim([H|_] , H).


% f([], -1).
% f([H|T], S):-
%     H > 0,
%     f(T, S1),
%     S1 < H,
%     !, 
%     S is H.
% f([_|T],S):-
%     f(T, S1), 
%     S is S1.

% fmod([], -1).
% fmod([H|T], S):-
%     fmod(T, S),
%     S >= H,
%     !.
% fmod([H|_], -1):-
%     H =< 0.    
% fmod([H|_], H).


% t([], 0).
% t([H|T], S):- t(T, S1), S1 is S - H.

%------------------------------------------------------
% prime(N,F):- N < F*2, !.
% prime(N,F):- N mod F =:= 0 ,!, false.
% prime(N,F):- F1 is F + 1, prime(N, F1).


% f(0, _, []).
% f(N, I, [I|S]):-
%     I =< N,
%     prime(I, 2),
%     N1 is N - I,
%     N1 >= 0,
%     I1 is I+1,
%     f(N1, I1, S).

% f(N, I, S):- I1 is I+1, I1 =< N , f(N, I1, S).




% fall(N):-
%     findall(S, f(N, 2, S), R),
%     print(R).

%------------------------------------------------------

% p(1).
% p(2).

% q(1).
% q(2).

% r(1).
% r(2).

% s :-  p(X), !, q(Y), r(Z), write((X,Y,Z)), nl.

%------------------------------------------------------

% s([H|_], N, S, [H]):- 
%     S1 is S + H, 
%     S1 mod 3 =:= 0,
%     N1 is N - 1,
%     N1 =< 0.

% s([H|T], N, S, [H|R]):-
%     N1 is N - 1,
%     S1 is S + H,
%     s(T, N1, S1, R).

% s([_|T], N, S, R):-
%     s(T, N, S, R).

% sall(L, N):-
%     findall(R, s(L, N, 0, R), Result),
%     print(Result).


% generate the list of all arangements of k elements from a list of integers, with the property that the product of elements from each arrangement is less than a givrn value V.

% this is aranjamente
% insert(e:integer , l: list, R: list)


(1 2 3) -> (1 2 3), (1 3 2), (2 1 3), (2 3 1), (3 1 2), (3 2 1)

%(1 2 3) -> insert(1,(2 3)) -> (1 2 3), (2 1 3), (2 3 1)
%(1 R) -> insert(2, (3)) -> (2 3), (3 2) -> (1 2 3), 
%
%
%


insert(E, L, [E|L]).
insert(E, [H|T], [H|R]):-
    insert(E, T, R).


remove(_, [], []).
remove(E, [H|T], T):- E =:= H, !.
remove(E, [H|T], [H|R]):-
    remove(E, T, R).



% aranjamente
aranjamente([H|_], L ,R):-
    remove(H, L, L1),
    insert(H, L1 , R).

aranjamente([_|T],L,R):-
    aranjamente(T, L, R).
    

aranj(L):-
    findall(R, aranjamente(L,L,R), Result),
    print(Result).


insertn(E, L, N, [E|L]):- N >= 0.
insertn(E, [H|T], N, [H|R]):-
    N1 is N - 1,
    N1 >= 0,
    insertn(E, T, N1, R).


