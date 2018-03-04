# Pixels

**category:** Forensics

**description:** Isn't this beautiful?

**value:** 60


## Write-up

Notice that around 11 o'clock on the circle, there's a weird looking strip of white. If we analyze the image (other than the random noise), all the gamma-values are around 0 or 255. The strips are (255, 255, 255, val) where val is the ascii encoding of the flag, reading from top down left to right.

[Source](debug/pixels.py) in repo.


## Flag

treeCTF{hello_pixels_my_old_friend}