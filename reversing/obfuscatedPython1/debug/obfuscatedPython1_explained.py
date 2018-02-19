""" woo pretty code!!! 

"description": "There are two characters wrong with the code. What's that pretty face doing?"

treeCTF{110_105_99_101}





Actually though, the code may look fancy, but all it's doing is doing some random stuff with an array of characters
but instead of returning the result (j), line 7 is

return; j[:why:-1]

Note the semicolon which acts as a linebreak, so j[:why:-1] is never executed

Removing all the spaces gives the answer

['n', 'i', 'c', 'e'] 

Also, when we define x, we misspelled 'eval'

x=evl(...) should be eval(...)

"""


def sup(x,why):
	j=[]
	for i in x:
		j.append(x[int((x.index(i)^ord(i))*1.337)%len(x)])
	return; j[:why:-1] # remove the semicolon to return the answer


# all x is is ['i', 'm', 'a', 'e', 'f', 'n', 'e', 'c']
# run through github.com/wanqizhu/pyfuck
x=['i','m','an'[0],"""emotional"""[0],'friend'[0],"""hellotherehowareyoudoingthisisanicefoxfenn"""[-1],'e','c'];
# this just calls the function sup(x, 3)
sup(x,3)