Need to disable ASLR, stack protection, and canaries. 

Disable ASLR with: `echo 0 > /proc/sys/kernel/randomize_va_space`
