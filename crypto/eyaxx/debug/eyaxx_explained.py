"""

the string "eyaxx" in hex is 101 121 97 120 120, which translates to

eyiyaxxx iyayayaxxxx uyaxx iyayayaxxx iyayayaxxx


Rules:

This language "eyaxx" basically only cares about powers of 2.

2 ay (just y if it's leading a word)
4 ey
5 ex
8 iy
16 oy
32 uy

Now, if a number n is of the form n = 2^k * m, where m is odd and k < 6, then n is written as

$y + (m)

where $y is the corresponding power of two. So for example, 12 = 2^2 * 3 = (4) + (3) = ey + ax.


If k > 5, then we keep adding 'u's at tho start of the string until k is less than 6. So if k = 11, we'd have 11 = 5 + 5 + 1 ==> uuay. You'll never see two vowels together except to represent large powers of 2.


If n is odd and n = m + 1, then n is written as m followed by 'x'. If n is one greater than a power of two, then we also remove the ending y. (e.g. 5 is 'ex' not 'eyx')




1 x
2 y
3 ax
4 ey
5 ex
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



"hint": "Look for multiples of 2s. The number system is pseudo-base2. Try to find patterns in the numbers given and look for pairs of similar numbers. If it helps, you can think of 2 as 'ay' and 5 as 'eyx'."

"""


# this is an implementation of the above logic, in full details


import re

def encode_recur(num):
	if num == 0:
		return '';

	if num%2:
		return encode_recur(num-1) + 'x'

	pre = ''

	power = 0
	while not num%2: # divide by 2 until we get odd number
		num /= 2
		power += 1
		if power > 5:
			power -= 5
			pre = 'u' + pre

	pre += ['a','e','i','o','u'][power-1] + 'y'

	if num == 1:
		return pre
	else:
		return pre + encode_recur(num)



def encode(num):
	if num == 0:
		return "yx"

	s = encode_recur(num)

	s = s.replace("yx", "x") # resolve numbers that are 1-greater than a power of 2

	if s[0:2] == 'ay':
		s = s[1:] # strip leading a

	return s



def decode_recur(s):
	if s == '': return 0

	vowels = ['a','e','i','o','u']


	if s.count('y') < s.count('x'): # more x's than y's, so remove one and subtract 1
		assert s[-1] == 'x', "WRONG FORMAT %s" % s # this must happen
		
		if len(s) > 1 and s[-2] in vowels:
			s[-1] = 'y'
		else:
			s = s[:-1]
		return decode_recur(s) + 1

	else:
		i = s.index('y')

		pre, s1 = s[:i], s[i+1:]


		assert pre != '', "WRONG FORMAT %s" % s
		for i in pre[:-1]:
			assert i == 'u', "WRONG FORMAT %s" % s # this must happen

		mult = 5*(len(pre) - 1) # if s has length greater than 2, then it must be prepending with u's
		mult += vowels.index(pre[-1]) + 1
			
		return pow(2,mult) * decode_recur(s1)





def decode(s):
	if s == 'yx': return 0;

	if s[0] == 'y':
		s = 'a' + s

	s1 = re.sub(r"(a|e|i|o|u)x", r"\1yx", s) # substitutes (vowel)x --> (vowel)yx
	if s1 != s or s[-1] == 'y':
		s = s1 + 'x'

	return decode_recur(s)


# make sure our logic works
for i in range(200):
	c = encode(i)
	assert decode(c) == i
	print(i, encode(i))



"""

(0, 'yx')
(1, 'x')
(2, 'y')
(3, 'ax')
(4, 'ey')
(5, 'ex')
(6, 'yax')
(7, 'yaxx')
(8, 'iy')
(9, 'ix')
(10, 'yex')
(11, 'yexx')
(12, 'eyax')
(13, 'eyaxx')
(14, 'yayaxx')
(15, 'yayaxxx')
(16, 'oy')
(17, 'ox')
(18, 'yix')
(19, 'yixx')
(20, 'eyex')
(21, 'eyexx')
(22, 'yayexx')
(23, 'yayexxx')
(24, 'iyax')
(25, 'iyaxx')
(26, 'yeyaxx')
(27, 'yeyaxxx')
(28, 'eyayaxx')
(29, 'eyayaxxx')
(30, 'yayayaxxx')
(31, 'yayayaxxxx')
(32, 'uy')
(33, 'ux')
(34, 'yox')
(35, 'yoxx')
(36, 'eyix')
(37, 'eyixx')
(38, 'yayixx')
(39, 'yayixxx')
(40, 'iyex')
(41, 'iyexx')
(42, 'yeyexx')
(43, 'yeyexxx')
(44, 'eyayexx')
(45, 'eyayexxx')
(46, 'yayayexxx')
(47, 'yayayexxxx')
(48, 'oyax')
(49, 'oyaxx')
(50, 'yiyaxx')
(51, 'yiyaxxx')
(52, 'eyeyaxx')
(53, 'eyeyaxxx')
(54, 'yayeyaxxx')
(55, 'yayeyaxxxx')
(56, 'iyayaxx')
(57, 'iyayaxxx')
(58, 'yeyayaxxx')
(59, 'yeyayaxxxx')
(60, 'eyayayaxxx')
(61, 'eyayayaxxxx')
(62, 'yayayayaxxxx')
(63, 'yayayayaxxxxx')
(64, 'uay')
(65, 'uax')
(66, 'yux')
(67, 'yuxx')
(68, 'eyox')
(69, 'eyoxx')
(70, 'yayoxx')
(71, 'yayoxxx')
(72, 'iyix')
(73, 'iyixx')
(74, 'yeyixx')
(75, 'yeyixxx')
(76, 'eyayixx')
(77, 'eyayixxx')
(78, 'yayayixxx')
(79, 'yayayixxxx')
(80, 'oyex')
(81, 'oyexx')
(82, 'yiyexx')
(83, 'yiyexxx')
(84, 'eyeyexx')
(85, 'eyeyexxx')
(86, 'yayeyexxx')
(87, 'yayeyexxxx')
(88, 'iyayexx')
(89, 'iyayexxx')
(90, 'yeyayexxx')
(91, 'yeyayexxxx')
(92, 'eyayayexxx')
(93, 'eyayayexxxx')
(94, 'yayayayexxxx')
(95, 'yayayayexxxxx')
(96, 'uyax')
(97, 'uyaxx')
(98, 'yoyaxx')
(99, 'yoyaxxx')
(100, 'eyiyaxx')
(101, 'eyiyaxxx')
(102, 'yayiyaxxx')
(103, 'yayiyaxxxx')
(104, 'iyeyaxx')
(105, 'iyeyaxxx')
(106, 'yeyeyaxxx')
(107, 'yeyeyaxxxx')
(108, 'eyayeyaxxx')
(109, 'eyayeyaxxxx')
(110, 'yayayeyaxxxx')
(111, 'yayayeyaxxxxx')
(112, 'oyayaxx')
(113, 'oyayaxxx')
(114, 'yiyayaxxx')
(115, 'yiyayaxxxx')
(116, 'eyeyayaxxx')
(117, 'eyeyayaxxxx')
(118, 'yayeyayaxxxx')
(119, 'yayeyayaxxxxx')
(120, 'iyayayaxxx')
(121, 'iyayayaxxxx')
(122, 'yeyayayaxxxx')
(123, 'yeyayayaxxxxx')
(124, 'eyayayayaxxxx')
(125, 'eyayayayaxxxxx')
(126, 'yayayayayaxxxxx')
(127, 'yayayayayaxxxxxx')
(128, 'uey')
(129, 'uex')
(130, 'yuax')
(131, 'yuaxx')
(132, 'eyux')
(133, 'eyuxx')
(134, 'yayuxx')
(135, 'yayuxxx')
(136, 'iyox')
(137, 'iyoxx')
(138, 'yeyoxx')
(139, 'yeyoxxx')
(140, 'eyayoxx')
(141, 'eyayoxxx')
(142, 'yayayoxxx')
(143, 'yayayoxxxx')
(144, 'oyix')
(145, 'oyixx')
(146, 'yiyixx')
(147, 'yiyixxx')
(148, 'eyeyixx')
(149, 'eyeyixxx')
(150, 'yayeyixxx')
(151, 'yayeyixxxx')
(152, 'iyayixx')
(153, 'iyayixxx')
(154, 'yeyayixxx')
(155, 'yeyayixxxx')
(156, 'eyayayixxx')
(157, 'eyayayixxxx')
(158, 'yayayayixxxx')
(159, 'yayayayixxxxx')
(160, 'uyex')
(161, 'uyexx')
(162, 'yoyexx')
(163, 'yoyexxx')
(164, 'eyiyexx')
(165, 'eyiyexxx')
(166, 'yayiyexxx')
(167, 'yayiyexxxx')
(168, 'iyeyexx')
(169, 'iyeyexxx')
(170, 'yeyeyexxx')
(171, 'yeyeyexxxx')
(172, 'eyayeyexxx')
(173, 'eyayeyexxxx')
(174, 'yayayeyexxxx')
(175, 'yayayeyexxxxx')
(176, 'oyayexx')
(177, 'oyayexxx')
(178, 'yiyayexxx')
(179, 'yiyayexxxx')
(180, 'eyeyayexxx')
(181, 'eyeyayexxxx')
(182, 'yayeyayexxxx')
(183, 'yayeyayexxxxx')
(184, 'iyayayexxx')
(185, 'iyayayexxxx')
(186, 'yeyayayexxxx')
(187, 'yeyayayexxxxx')
(188, 'eyayayayexxxx')
(189, 'eyayayayexxxxx')
(190, 'yayayayayexxxxx')
(191, 'yayayayayexxxxxx')
(192, 'uayax')
(193, 'uayaxx')
(194, 'yuyaxx')
(195, 'yuyaxxx')
(196, 'eyoyaxx')
(197, 'eyoyaxxx')
(198, 'yayoyaxxx')
(199, 'yayoyaxxxx')

"""


# generate the problem

f = open("eyaxx.txt", "w")

f.write("""You wake up in a dark room with a blasting headache. 
After exploring around and finally fumbling upon the light switch, 
you see the following on the board in front of you:\n\n""")

for i in range(1, 41):
	f.write(str(i) + " " + encode(i) + "\n")



f.write(str(420) + " " + encode(420) + "\n")
f.write(str(1024) + " " + encode(1024) + "\n")
f.write(str(1337) + " " + encode(1337) + "\n")
f.write(str(1729) + " " + encode(1729) + "\n")


flag = "treeCTF{eyaxx=ElephantYolo&x_x}"

f.write("""\n\n\nYou see a guard outside and bangs on the window, but his blank stare refuses to move no matter what you say. 
Finally, he points at the floor, on which you notice the following message. What is the magic phrase you must say to escape?\n\n\n""")

f.write(' '.join(map(lambda x: encode(ord(x)), flag)))

f.close()