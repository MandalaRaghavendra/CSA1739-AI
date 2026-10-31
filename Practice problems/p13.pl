fact(ravi, fever).
fact(ravi, cough).

rule(fever, cough, flu).

diagnosis(X, flu) :-
    fact(X, fever),
    fact(X, cough).
