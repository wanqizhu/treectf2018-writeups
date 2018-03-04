# Steam Locomotive

**category:** Misc

**description:**
Looks like some team is solving challenges a bit too fast! Should have started since noon

<code>31 * x1 + 45
32 * x2 + 33
36 * x3 + 100
37 * x4 + 46
60 * x5 + 65
48 * x6 + 79
64 * x7 + 21
46 * x8 + 65
52 * x9 + 101
135 * x10 + 39
63 * x11 + 109
80 * x12 + 12
78 * x13 + 45
176 * x14 + 31
192 * x15 + 20
94 * x16 + 34
79 * x17 + 34
</code>
        
**value:** 111


## Write-up


We basically encode the flag's ascii values by the number of seconds since noon team Steam Locomotive have solved the problem.

Solve times can be found on the team's scoreboard page.

'''
times
['1:00:41', '1:01:21', '1:02:16', '1:03:03', '1:08:05', '1:08:31', '1:15:01', '1:35:23', '1:41:21', '1:48:39', '1:58:22', '2:06:52', '2:14:39', '2:21:19', '2:33:56', '2:37:14', '2:45:09']

>>> times = [int(x[0])*3600+int(x[2:4])*60+int(x[5:]) for x in b]
>>> times
[3641, 3681, 3736, 3783, 4085, 4111, 4501, 5723, 6081, 6519, 7102, 7612, 8079, 8479, 9236, 9434, 9909]

flag = "treeCTF{s0o_g00d}"
>>> ans = [ord(i) for i in flag]
>>> ans
[116, 114, 101, 101, 67, 84, 70, 123, 115, 48, 111, 95, 103, 48, 48, 100, 125]


[((a//b), a%b) for (a,b) in zip(times, ans)]
[(31, 45), (32, 33), (36, 100), (37, 46), (60, 65), (48, 79), (64, 21), (46, 65), (52, 101), (135, 39), (63, 109), (80, 12), (78, 45), (176, 31), (192, 20), (94, 34), (79, 34)]

>>> [(str(a//b)+ 'x+' + str(a%b)) for (a,b) in zip(times, ans)]
['31x+45', '32x+33', '36x+100', '37x+46', '60x+65', '48x+79', '64x+21', '46x+65', '52x+101', '135x+39', '63x+109', '80x+12', '78x+45', '176x+31', '192x+20', '94x+34', '79x+34']
'''

## Flag

treeCTF{s0o_g00d}