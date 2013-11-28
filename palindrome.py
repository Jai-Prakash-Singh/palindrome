#/usr/bin/env python 


import sys, shlex



def rev_word(word):
    r_word = word [::-1]
    if r_word == word:
        return  word



def palindrome(filename):
    try:
        f = open(filename)
	content = f.read()
	lst_word = shlex.split(content)
        for element in lst_word:
            word = rev_word(element)
            if word:
                yield word 
            else:
                pass
    except:
        print " there is error in opening in file"
    finally:
	f.close()
        yield " file is closed"



if __name__=="__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print "required running method:"
	print " python palindrome filename"
	print " filename according to you"
        sys.exit(-1)
    else:
        lst_palindrome = palindrome(sys.argv[1])
	for pal_word  in lst_palindrome:
            print pal_word
        sys.exit(0)

