# -b

**category:** Crypto

**description:** To e or not to e, that is the question. Can you figure out Polyius' favorite color?\r\n\r\n<code>\r\n44 42 14 14 12 44 15 \r\n31 45 14 \r\n23 43 \r\n11 \r\n14 11 45 44 23 15 45 31 \r\n12 34 31 34 42\r\n</code>

**value:** 60


### Hint ###

Roses are red. Violets are blue. Without those bees. A square can finally be formed.


## Write-up

We see that we are given a series of 2-digit numbers, all of which are between 1 and 5; note the reference to Polybius and squares, we think of coordinates and square cipher.

The cipher is a standard Polybius [square cipher](https://en.wikipedia.org/wiki/Polybius_square), with the letters are laid out in a 5x5 grid. The tricky part is noticing that the square skips 'b': this can be inferred by the problem name and the references like 'without those bees'.

### Details ###


The encryption grid is below:


    1 2 3 4 5

  1 a c d e f
  2 g h i j k
  3 l m n o p
  4 q r s t u
  5 v w x y z


xy correspond to the letter at x-th row and y-th column.


We can then decode as above. 31 --> (3rd row, 1st column) --> l, 11--> a, etc.


[Full code here.](debug/-b_explained.py)


## Flag

treeCTF{blue_is_a_beautiful_color}

(tree[cC][tT][fF])?\\{?b?lue[ _]?is[ _]?a[ _]?b?eautiful[ _]?color\\}?
