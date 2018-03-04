# Solution:

One of the message is susceptible to Wiener's attack. This exposes the private key D. The two messages share the same public modulus N. The private key D for the weak message can be used to factor N into primes p and q. Using primes p and q, the modular inverse of the public key (of the strong message) can be calculated; thus, giving the private key D. This D can be used to decrypt the stronger message. 

Source in repo

## Reference:
https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf

https://www.di-mgt.com.au/rsa_factorize_n.html

https://en.wikipedia.org/wiki/RSA_(cryptosystem)
