insert(E, L, [E|L]).
insert(E, [H|T], [H|R]):-
    insert(E, T, R).


comb([H|_],1, [H]).
comb([H|T], K, [H|R]):-
    K1 is K - 1,
    K1 > 0,
    comb(T, K1, R).
     
comb([_|T], K, R):-
    comb(T, K, R).

% comball(L, K):-
%     findall(R, comb(L, K, R), Result),
%     print(Result).

perm([], []).
perm([H|T], R):-
    perm(T, R1),
    insert(H, R1, R).

% permall(L):-
%     findall(R, perm(L, R), Result),
%     print(Result).

%---------------------------------------------------------

aranj([H|_], 1, [H]).

aranj([_|T], K, R):-
    aranj(T, K, R).

aranj([H|T], K, R):-
    K1 is K - 1,
    K1 > 0,
    aranj(T, K1, R1),
    insert(H, R1, R).


aranjall(L, K):-
    findall(R,aranj(L,K,R), Result),
    print(Result).

%---------------------------------------------------------

aranjamente(L, K, R):-
    comb(L, K, R1),
    perm(R1, R).

% aranjamenteall(L,K):-
%     findall(R, aranjamente(L, K, R), Result),
%     print(Result).


prod([], 1).
prod([H|T], R):-
    prod(T, R1),
    R is R1*H.

arrProd(L,K,V, R):-
    aranjamente(L,K,R1),
    prod(R1, P),
    P < V,
    R = R1.

arrProdAll(L,K,V):-
    findall(R, arrProd(L,K,V,R), Result),
    print(Result).
