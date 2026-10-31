move(atdoor, middle).
move(middle, underbox).
move(underbox, onbox).

get_banana :-
    move(atdoor, middle),
    move(middle, underbox),
    move(underbox, onbox),
    write('Monkey got the banana').
