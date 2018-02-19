
# "description": "Caesar is back for more, this time with numbers! Can you figure out his <a href='shifty.txt'>message?</a>",
# "hint": "The numbers and letters shift on different modulus."


import random, string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)

    alphabet2 = string.ascii_uppercase
    shifted_alphabet2 = alphabet2[shift:] + alphabet2[:shift]
    table2 = string.maketrans(alphabet2, shifted_alphabet2)

    nums = '0123456789'
    shift = shift % len(nums)
    shifted_nums = nums[shift:] + nums[:shift]
    table3 = string.maketrans(nums, shifted_nums)

    return plaintext.translate(table).translate(table2).translate(table3)


flag = "wowYouDecodedSomeGarbage!treeCTF{shifty_arith_best_arith?1*3=91}"
random.seed(1)

arith = ["*", "+", "-", "**"]

f = open("shifty.txt", "w")

f.write("Looks like some letters have been shifted -- oh no, the numbers too? What will we do?\n\n")

for c in flag:
	shift = random.randint(1, 26)
	n1 = random.randint(1, 100)
	n2 = random.randint(1, 100)
	operation = arith[shift%4]
	n3 = eval(str(n1) + operation + str(n2))

	s = "%s\t%s%s%s = %s\n" % (c, n1, operation, n2, n3)
	#print(s, caesar(s, shift))
	f.write(caesar(s, shift))
