#!/usr/env/bin python
"""Solution to 🔥 from TreeCTF 2018."""
import string

encoding_map = {ch:chr(0x1F600+i) for i, ch in enumerate(string.ascii_lowercase)}
def encode(plaintext):
    return ''.join(map(lambda ch: encoding_map.get(ch, ch), plaintext))

decoding_map = {value:key for key, value in encoding_map.items()}
def decode(ciphertext):
    return ''.join(map(lambda ch: decoding_map.get(ch, ch), ciphertext))

ciphertext = '😓😇😄 😅😀😓😇😄😑 😎😅 😓😇😄 😄😌😎😉😈 😈😒 😒😇😈😆😄😓😀😊😀 😊😔😑😈😓😀, 😖😇😎 😈😍😓😑😎😃😔😂😄😃 😓😇😄 😖😎😑😋😃 😓😎 😓😇😄 😅😈😑😒😓 😎😍😄 😈😍 1999! 😓😇😄 😅😋😀😆 😈😒 😓😑😄😄😂😓😅{😄😌😎😉😈_😆😄😍😈😔😒}'

print(decode(ciphertext))
# => 'the father of the emoji is shigetaka kurita, who introduced the world to the first one in 1999! the flag is treectf{emoji_genius}'

FLAG = 'treectf{emoji_genius}'
