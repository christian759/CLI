from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.usage = "Description"

parser.add_argument("a", type=int, help="The base value")
parser.add_argument("b", type=int, help="The exponent")

parser.add_argument('-v', '--verbosity', action="count", help="It helps improve output verbosity", default=0)
"""
or parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
"""

args : Namespace = parser.parse_args()

answer = args.a** args.b

if args.verbosity >= 2:
	print(f"{args.a} to the power {args.b} equals {answer}")
elif args.verbosity >= 1:
	print(f"{args.a}^{args.b} == {answer}")
else:
	print(answer)

"""
more:

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")

"""

