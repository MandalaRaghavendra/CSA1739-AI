male(ram).
male(raju).
female(sita).
female(anu).

parent(ram, raju).
parent(sita, raju).
parent(raju, anu).

father(X, Y) :-
    male(X), parent(X, Y).

mother(X, Y) :-
    female(X), parent(X, Y).
