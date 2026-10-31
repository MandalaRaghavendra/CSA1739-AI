symptom(ravi, fever).
symptom(ravi, cough).
symptom(ram, headache).

disease(X, flu) :-
    symptom(X, fever),
    symptom(X, cough).

disease(X, migraine) :-
    symptom(X, headache).
