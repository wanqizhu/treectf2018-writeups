# Eyaxx

**category:** Crypto

**description:** Check out this new [number system!](eyaxx.txt)

**value:** 250



## Write-up

This language "eyaxx" basically only cares about powers of 2. We repeatedly divide out powers of 2 until we get an odd number (marked by vowels+y), then we subtract one (marked by x), and repeat until we get to 0.

2 ay (just y if 'ay' leading a word)
4 ey
5 ex = (ey)(x), y omitted since yx consecutive
6 yax = 2^1 * 3 = (ay)(ax), a not included since it's leading the word
7 yaxx = 6 + 1 = (yax)(x)
8 iy
9 ix = 8 + 1 = (iy)(x), y not included since 9 is one more than a power of 2
10 yex
11 yexx = 10 + 1 = 2^1 * 5 (x) = (ay) 5 (x) = (ay) (2*2 + 1) (x) = (ay) (2*2 (x)) (x) = (ay) (ey) (x) (x) = ye
12 eyax
13 eyaxx
14 yayaxx
15 yayaxxx
16 ox

Now, if a number n is of the form n = 2^k * m, where m is odd and k < 6, then n is written as

$y + (m)

where $y is the corresponding power of two. So for example, 12 = 2^2 * 3 = (4) + (3) = ey + ax.


If k > 5, then we keep adding 'u's at tho start of the string until k is less than 6. So if k = 11, we'd have 11 = 5 + 5 + 1 ==> uuay. You'll never see two vowels together except to represent large powers of 2.


If n is odd and n = m + 1, then n is written as m followed by 'x'. If n is one greater than a power of two, then we also remove the ending y. (e.g. 5 is 'ex' not 'eyx')



[Full code and explanation](debug/eyaxx.py)



**flag:** treeCTF{eyaxx=ElephantYolo&x_x}