fact(ravi, fever).
fact(ravi, cough).

disease(X, flu) :-
    fact(X, fever),
    fact(X, cough).

disease(X, cold) :-
    fact(X, cough).
