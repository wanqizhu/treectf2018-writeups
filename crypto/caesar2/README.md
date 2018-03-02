# Welcome to Rome

**category:** Crypto

**description:** Hail Caesar! <code>10 434 431 22 444 432 434 65 449 444 65 16 449 20 443 435 444 447 433 66 65 449 447 434 434 90 17 03 456 22 20 434 448 20 447 28 93 84 28 68 448 28 83 458</code>
        

**value:** 100



## Write-up

Each letter is ascii encoded into a 2 or 3 digit number, then we caesar shift the digits 0-9, essetially adding each digit by 3 mod 10.

So 1->4, 2->5, 7->0, 8->1, etc.

To decrypt, we can try all 10 possible shifts, or note that ascii values are between 60 and 128 and guess the offshift.

[Full code here.](debug/caesar2_explained.py)

```python2
flag = "10 434 431 22 444 432 434 65 449 444 65 16 449 20 443 435 444 447 433 66 65 449 447 434 434 90 17 03 456 22 20 434 448 20 447 28 93 84 28 68 448 28 83 458"

def caesar_nums(plaintext, shift):
  nums = '0123456789'
  shifted_nums = nums[shift:] + nums[:shift]
  table = string.maketrans(nums, shifted_nums)
  return plaintext.translate(table)


plaintext = caesar_nums(flag, 7)
print("".join(map(lambda x: chr(int(x)), plaintext.split(" "))))

```


**flag:** treeCTF{caesar_<3_#s_2}