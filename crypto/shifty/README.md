# Shifty Tjljye

**category:** Crypto

**description:** Caesar is back for more, this time with numbers! Can you figure out [his message?](shifty.txt)

**value:** 180


## Write-up

Each line is caeser-shifted A-Z and 0-9 by the same shift. However, note that the letter is shifted mod 26 whereas the digits are mod 10, so there may be multiple shifts that would satisfy the equation.

To generate the problem, we generate true arithmetic equations next to each letter, then shift the entire line by a random shift.

[Full code here.](debug/shifty_explained.py)


## Flag

treeCTF{shifty_arith_best_arith?1*3=91}