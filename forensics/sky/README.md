# A Sky Full of Stars

**category:** Forensics

**description:** You see a sky, you see a [sky full of stars...](sky_map.jpg) but what do you [not see?](sky_key.txt)

**value:** 130


## Write-up

We're hiding information at the end of the image file.

We add in a bunch of stars '\*' to the end of the image
Hidden within the \*'s  is the lyrics to the song.

Then each row in sky_key maps to a corresponding (row, column) of the lyrics --> giving us a character which spells out the flag. e.g. (3, 5) is the 5th character on the 3rd row.


[Source](debug/sky_full_of_stars_explained.py) in repo.


## Flag

treeCTF{oo'h tear the sky a'part}