diet(diabetes, 'Low sugar food').
diet(obesity, 'Low fat food').
diet(anemia, 'Iron rich food').
diet(heart_disease, 'Low salt food').

suggest(X, Y) :-
    diet(X, Y).
