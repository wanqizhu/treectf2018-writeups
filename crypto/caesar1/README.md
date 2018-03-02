# Attack at -3

**category:** Crypto

**description:** <code>wuhhFWI{dwn_@_gdzq}</code>

**value:** 20



## Write-up

This is just simple caesar cipher, where we shift every letter.


```python
flag = "wuhhFWI{dwn_@_gdzq}"
print(''.join([chr(ord(c)-3) if c.islower() or c.isupper() else c for c in flag]))
```

**flag:** treeCTF{atk_@_dawn}