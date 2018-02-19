# Basically a Polybius Square Cipher, but instead of i/j being one square or omitting z, we omit b instead (thus -b ~ "minus b", and all the bee/B puns).


#     1 2 3 4 5

# 1	a c d e f
# 2	g h i j k
# 3	l m n o p
# 4	q r s t u
# 5	v w x y z






# We can remove the b's, since it's hopefully clear from context

import string

flag = "treectf{blue_is_a_beautiful_color}"
encoding = 'a' + string.ascii_lowercase[2:]  # skip b

ciphertext = ''
for c in flag:
    if c == 'b':
        continue
    if c not in encoding:
        ciphertext += '\n'
        continue
    
    n = encoding.index(c)
    ciphertext += str(n//5 + 1)
    ciphertext += str(n%5 + 1)
    ciphertext += ' '

print(ciphertext)