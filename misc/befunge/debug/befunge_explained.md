## InPUT nOT FOUnD - 80 (Misc) ##
#### Problem by Wanqi Zhu
Writeup by Wanqi Zhu



### Problem ###

I'm befuddled by [befunge](http://ec2-52-35-36-1.us-west-2.compute.amazonaws.com/problem-static/misc/befunge/InPUTnOTFOUnD).

### Hint ###

[Befunge](https://esolangs.org/wiki/Befunge). The input is 3 characters. UPDATE: You can try inputting any 3 characters just to see how the logic flows -- each character work independantly of the other two.

## Note ##

It's helpful to run Befunge through one of the [online interpreters](http://www.quirkster.com/iano/js/befunge.html).

### Answer ###

There are a few ways to approach the problem. Some might notice the 3 undercase n's in the problem name and in the "WELCOME TO BEFUnGE HAVE FUnn!" text in the program. Turns out that the correct input to the program is "nnn", which if you run the code with will give you the flag.

Alternatively, we can trace through the logic of the problem. (This assumes you've read the esolang Befunge wiki and understands it. It's a pretty cool stack language.)



### Details ###

Note the ~'s take an input character, so we know there are 3 inputs. After that, it's just following the logic carefully and managing your stack: say if the first input is x, then we go through the arithmetic until the program reaches 

|

or 

-

Either of those checks if the top value of the stack is 0. The loops can be confusing, so it's easier to break down each part of the program. The easiest way to do that is to "step" through the program with a good 0interpreter](http://www.quirkster.com/iano/js/befunge.html).

Doing it carefully, you can deduct that each input character has to be 'n'. (It's hard to describe how to run through the logic of teh program here.)


Alternatively, you can also IGNORE all tests of | or - and just replace them with arrow keys going in the right direction (after also popping the top value of the stack and discarding it). Since you can modify the program, you could get the flag w/o figuring out the 3 input chars.


### Flag ###
labCTF{ice_meme}
