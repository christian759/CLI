"""
author: CEO1
"""

from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

group = parser.add_mutually_exclusive_group()

parser.usage = "My mini calculator"

parser.add_argument("a", type=int, help="The first value")
parser.add_argument("b", type=int, help="The second value")

group.add_argument("-a", "--add", action="store_true")
group.add_argument("-s", "--subtract", action="store_true")
group.add_argument("-m", "--multiply", action="store_true")
group.add_argument("-d", "--divide", action="store_true")
group.add_argument("-p", "--pow", action="store_true")
group.add_argument("-%", "--mod", action="store_true")
group.add_argument("-_", "--operate", action="store_true")

args: Namespace = parser.parse_args()

if args.add:
	print(args.a + args.b)

elif args.subtract:
	print(args.a-args.b)

elif args.multiply:
	print(args.a*args.b)

elif args.divide:
	print(args.a/args.b)

elif args.pow:
	print(args.a**args.b)

elif args.mod:
	print(args.a%args.b)

elif args.operate:
	print(args.a+args.b)
	print(args.a-args.b)
	print(args.a*args.b)
	print(args.a/args.b)
	print(args.a**args.b)
	print(args.a%args.b)

 
else:
	raise Exception("No given operation")

"""happy coding"""
