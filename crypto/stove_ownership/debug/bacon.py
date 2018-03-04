#!/usr/bin/env python
"""Solution to Stove Ownership from TreeCTF 2018."""
import string


UPPER = string.ascii_uppercase


CODES = (
    'A **T**YP**E**',
    '**O**F SAL',
    '**T** CU**R**E',
    'D P**ORK**',
    'AN **E**N**G**',
    'LI**S**H P',
    'HIL**OS**',
    '**O**P**H**ER',
    '**S**TA**TE**',
    'S**MAN S**',
    'C**IE**NT',
    '**IS**T J**U**',
    '**RI**ST O',
    'R**ATO**R',
    'A**N**D **AU**',
    'THOR B',
    'O**R**N 15',
    '61 DI**E**',
    '**D** 162**6**',
    '**C**A**LVI**',
    'N **A**N**D** H',
    'O**BB**E**S**',
    '**A**N**D P**A',
    'NTS **A**R',
    '**E** O**V**E**R**',
    'RA**TE**D',
)


def decode_to_binary(symbols):
    symbols = symbols.replace(' ', '')
    s = ''
    for ct, run in enumerate(symbols.split('**')):
        s += str(ct % 2) * len(run)
    return s


encoding_map = {UPPER[int(decode_to_binary(code), 2)]: pt for code, pt in zip(CODES, UPPER)}
"""
=> {
    'A': 'P',
    'B': 'R',
    'C': 'X',
    'D': 'G',
    'E': 'F',
    'F': 'E',
    'G': 'Z',
    'H': 'D',
    'I': 'Q',
    'J': 'A',
    'K': 'U',
    'L': 'O',
    'M': 'K',
    'N': 'V',
    'O': 'N',
    'P': 'J',
    'Q': 'B',
    'R': 'S',
    'S': 'C',
    'T': 'I',
    'U': 'H',
    'V': 'Y',
    'W': 'W',
    'X': 'T',
    'Y': 'M',
    'Z': 'L'
}
"""
def encode(plaintext):
    return ''.join(map(lambda ch: encoding_map.get(ch, ch), plaintext))


decoding_map = {value:key for key, value in encoding_map.items()}
def decode(ciphertext):
    return ''.join(map(lambda ch: decoding_map.get(ch, ch), ciphertext))


if __name__ == '__main__':
    ciphertext = 'NKVNKVNKVNKVNKVNK! IDF XSQCJM EOPZ QC ISFFXIE{UVNWOFGZF_QC_JNWFS}'
    print(decode(ciphertext))
