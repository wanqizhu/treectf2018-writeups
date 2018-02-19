## -b - 50 (Crypto) ##
#### Problem by Josh Kaplan & Wanqi Zhu
Writeup by Wanqi Zhu



### Problem ###

To bee or not to bee, that is the question. Can you figure out Polybius' [answer?](http://ec2-52-35-36-1.us-west-2.compute.amazonaws.com/problem-static/crypto/minusb/-b.txt).

### Hint ###

Roses are red. Violets are blue. Without those bees. A square can finally be formed.

## Note ##



## Answer ##

### Overview ###

We see that we are given a series of 2-digit numbers, all of which are between 1 and 5; note the reference to Polybius and squares, we think of coordinates and square cipher.

The cipher is a standard Polybius [square cipher](https://en.wikipedia.org/wiki/Polybius_square), with the letters are laid out in a 5x5 grid. The tricky part is noticing that the square skips 'b': this can be inferred by the problem name and the references like 'without those bees'.

### Details ###


The encryption grid is below:


	    1 2 3 4 5

	1	a c d e f
	2	g h i j k
	3	l m n o p
	4	q r s t u
	5	v w x y z


xy correspond to the letter at x-th row and y-th column.


We can then decode as above. 31 --> (3rd row, 1st column) --> l, 11--> a, etc.

### Flag ###

    labCTF{bee_there_or_bee_square}

Or laCTF{ee_there_or_ee_square}, if you want to take out the b's :)