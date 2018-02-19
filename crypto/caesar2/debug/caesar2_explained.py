import string

s = "Welcome to Stanford! treeCTF{caesar_<3_#s_2}"
flag = " ".join([str(ord(c)) for c in s])


def caesar_nums(plaintext, shift):
	nums = '0123456789'
	shifted_nums = nums[shift:] + nums[:shift]
	table = string.maketrans(nums, shifted_nums)

	return plaintext.translate(table)



print(caesar_nums(flag, 3))