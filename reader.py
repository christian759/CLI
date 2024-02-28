from argparse import ArgumentParser, Namespace
import enchant

all_words = enchant.Dict("en_US")

parser = ArgumentParser()
parser.usage = "My file checker"

#parser.add_argument("filename", type=str, help="File to check")

#parser.add_argument("-c", "--check", action="store_true")

#args: Namespace = parser.parse_args()

if True:
    with open("text.txt", 'r') as f:
	    for i in f.readlines():
	    	k = bool(all_words.check(i))
	    	if k:
	    		pass
	    	else:
	    		print("incorrect spelling {i}")
	
else:
	raise Exception("missing file-name")
		 


