# 🔥

**Category:** Crypto

**Points:** 60

**Solves:** 23

**Description:**

```
Have you heard the latest hits?

* despacit😎
* the shape of 😔
* that's what 😈 like

😓😇😄 😅😀😓😇😄😑 😎😅 😓😇😄 😄😌😎😉😈 😈😒 😒😇😈😆😄😓😀😊😀 😊😔😑😈😓😀, 😖😇😎 😈😍😓😑😎😃😔😂😄😃 😓😇😄 😖😎😑😋😃 😓😎 😓😇😄 😅😈😑😒😓 😎😍😄 😈😍 1999! 😓😇😄 😅😋😀😆 😈😒 😓😑😄😄😂😓😅{😄😌😎😉😈_😆😄😍😈😔😒}
```

Problem inspiration credits to Praetorian.

## Write-up

At first glance, this seems to look like a [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher). Indeed, it is. The song titles in the description provide the clues that `'o'->'😎'`, `'u'->'😔'`, and `'i'->'😈'`. Furthermore, the fact that all the song titles are in lowercase suggests that this will be a case-insensitive substitution cipher, and that the final answer should be all lowercase. We'll continue to operate in lowercase in this write-up.

Given these vowels and some clever guessing, it's possible to reconstruct most of, if not all, of the flag. Additionally, there are techniques for [decoding substitution ciphers using frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis#Frequency_analysis_for_simple_substitution_ciphers), but they generally requires a larger ciphertext than provided here.

In fact, we can exploit a fact about emoji in order to simplify this problem. In fact, there is a value associated with each emoji - its 'unicode value'. In [this list](https://unicode.org/emoji/charts/full-emoji-list.html) provided by the Unicode organization, there is a value for each emoji under the 'code' column (written in [hexadecimal notation](https://simple.wikipedia.org/wiki/Hexadecimal_numeral_system)). For example, `😀` has code `0x1F600`. Another way to state this fact is that **emoji have a natural ordering given by their unicode values.** It is precisely this ordering that we use in the substitution cipher. That is, the encoding map is given by:

```
{
    'a': '😀',  # value 1F600
    'b': '😁',  # value 1F601
    'c': '😂',  # value 1F602
    'd': '😃',  # value 1F603
    'e': '😄',  # value 1F604
    'f': '😅',  # value 1F605
    'g': '😆',  # value 1F606
    'h': '😇',  # value 1F607
    'i': '😈',  # value 1F608
    'j': '😉',  # value 1F609
    'k': '😊',  # value 1F60A
    'l': '😋',  # value 1F60B
    'm': '😌',  # value 1F60C
    'n': '😍',  # value 1F60D
    'o': '😎',  # value 1F60E
    'p': '😏',  # value 1F60F
    'q': '😐',  # value 1F610
    'r': '😑',  # value 1F611
    's': '😒',  # value 1F612
    't': '😓',  # value 1F613
    'u': '😔',  # value 1F614
    'v': '😕',  # value 1F615
    'w': '😖',  # value 1F616
    'x': '😗',  # value 1F617
    'y': '😘',  # value 1F618
    'z': '😙'   # value 1F619
}
```

Note that this is consistent with the hint from the song titles, suggesting that this is indeed the proper ordering of emoji (rather than a possible alternative which uses the emoji categories).

Applying this to the ciphertext yields the plaintext: 'the father of the emoji is shigetaka kurita, who introduced the world to the first one in 1999! the flag is treectf{emoji_genius}'

Thus, the final flag is `treectf{emoji_genius}`.

Lastly, we must give credit to Praetorian for this clever problem exploiting the induced ordering of emoji by their unicode values. One of our CTF authors (Sam) participated in a CTF run by Praetorian and shameless coopted the Emoji substitution cipher for TreeCTF.


## Additional Resources

- See CTF participant data [here](treectf.2018-02-18.zip).