# Robots

**category:** Web

**description:** Oh no! The [robots](site/index.html) have invaded!

**value:** 30


## Write-up

robots.txt is a file that controls which pages in a server is searchable by web-crawlers like google. If we look at `robots.txt` file on the linked `index.html`, we see

```
User-agent: *
Disallow: /71b301sz8402.html
```

Hmm, that's a weird url! Let's take a look.


## Flag
treeCTF{80tS_b3L0nG_iN_A_M3TR1X}