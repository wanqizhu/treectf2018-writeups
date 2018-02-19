def decode(s, accumulator=0):
    out = ""
    for cmd in s:
        if accumulator == 256 or accumulator == -1:
            # Overflow, reset accumulator
            accumulator = 0
        # Process input
        if cmd == 'i':
            accumulator += 1 # Increment
        elif cmd == 'd':
            accumulator += -1 # Decrement
        elif cmd == 'o':
            out += chr(accumulator) # Output
        elif cmd == 's':
            accumulator *= accumulator # Square

    return out, accumulator

cipher = open('ciphertext2.txt').read()
#print(cipher)

for accum in range(256):
    try:
        flag, _ = decode(cipher, accum)
        print(flag, accum)
    except:
        pass

"""You see
treeCTF{s*___GARBAGE___mor*_delic*o*s_than_<3} 42

so the accumulator is at 42 with some data corrupted in the middle"""


# so -- what could be wrong?

# flag, accum = decode(cipher[:200], 42)

start = 1
while flag != 'treeCTF{s*' and start < len(cipher):
    flag, accum = decode(cipher[:start], 42)
    start += 1

end = start
while flag == 'treeCTF{s*' and end < len(cipher):
    flag, accum = decode(cipher[:end], 42)
    end += 1

print(start, end)

# so error probably somewhere between 262 and 305
print(cipher[start-2:end])
# oddddddddddddddddddddddddddsddddsddddddddddodd

""" now it's just a matter of playing around and thiniking about how data might be lost
- either we have missing instructions or some instruction is changed

the two s's being so close apart is suspicious since rarely do we square twice in a row

so let's try changing them
"""
print(cipher[start-2:end].index('s'))
print(cipher[start-2+27], cipher[start-2+27+5])
print(start-2+27, start-2+27+5)

for c in ['s', 'i', 'd', 'o']:
    for c2 in ['s', 'i', 'd', 'o']:
        try:
            cipher = cipher[:287] + c + cipher[288:292] + c2 + cipher[293:]
            print(decode(cipher, 42))
        except:
            pass

# ('treeCTF{s*ome_**sh_is*mor*_delic*o*s_than_<3}', 125)
