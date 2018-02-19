flag = "treeCTF{atk_@_dawn}"
print(''.join([chr(ord(c)+3) if c.islower() or c.isupper() else c for c in flag]))