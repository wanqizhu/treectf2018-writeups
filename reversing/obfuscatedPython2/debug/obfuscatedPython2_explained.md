## Obfuscated Python 2 - 120 (Reversing) ##
#### Problem by Wanqi Zhu
Writeup by Wanqi Zhu


### Problem ###
[Antigravity!](http://ec2-52-35-36-1.us-west-2.compute.amazonaws.com/problem-static/reversing/obfuscated_python2/obfuscated_python2.py)
Where did it [go?](http://ec2-52-35-36-1.us-west-2.compute.amazonaws.com/problem-static/reversing/obfuscated_python2/obfuscated_python2.out)


### Hint ###
Some randomness isn't so random after all.


### Answer ###

The code seems to use a ton of randomness, which is hard (though not impossible thanks to random seeding, as we know f[-1] == '}')

BUT THAT'S NOT THE WAY TO SOLVE IT!


Looking at antigravity.geohash, we see that it takes in 2 floats and a string, then hashes the first two numbers based on the string

However, note that it only changes the DECIMAL PARTS of the input numbers, not the INTEGRAL parts!

Furthermore, the only thing that matters is the integer parts, as they came from

```ord( some_character_from_flag ) + np.random.random()```, the latter of which is a float between 0 and 1

So we can reconstruct the flag that way. Be careful of the wierd indexing though with the Zip call.



By the way, the parity of the length of the flag matters in zip(f[::-2], f[::2]). For the opposite parity you'd use zip(f[::-2], f[1::2])


```
f = open("obfuscated_python2.out").read().split("\n")
c1 = []
c2 = []

for row in f:
	a, b = map(lambda x: chr(int(float(x))), row.split(" "))
	c1.append(a)
	c2.append(b)


flag = ''
for c1, c2 in zip(c2, c1[::-1]):
	flag += c1 + c2


print(flag)
```

### Flag ###
labCTF{xkcd_is_op}
