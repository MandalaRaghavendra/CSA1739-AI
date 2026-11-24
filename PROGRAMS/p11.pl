edge(a, b, 2).
edge(a, c, 1).
edge(b, d, 3).
edge(c, d, 2).

best(a, Goal) :-
    search(a, Goal, [a]).

search(Goal, Goal, _) :-
    write('Goal Found').

search(Node, Goal, Visited) :-
    edge(Node, Next, _),
    \+ member(Next, Visited),
    search(Next, Goal, [Next|Visited]).
