Game why the turtle cross the road :D

NOTE: There is a small bug that I have no clue how to fix it.
When starting a new round, turtle often automatically move forward once, or twice. I suspect this is because some python logic can be too slow against storing another onkeypress().
I mean, I believe that after reaching the end, it's storing next command to move forward (from onkeypress()) before executing code logic related to start a new round. In result, when new round start, it immediately move forward as he still have stored comand to move forward.

There are two workarounds:
1. Instead onkeypress() use onkey() which is exhausting for user in the long run (as he need constantly clicking the key)
2. Set starting position of the turtle lower. Not the best way, but at least you let user avoid being run over as soon as a new round start if a car spawns in front of you.


