import argparse

parser = argparse.ArgumentParser()

parser.add_argument('greeting', help='The Greeting Message Displayed') # this is optional
parser.add_argument('-n', '--numbers', type=float, nargs='*', help='Two Numbers to Add')
parser.add_argument('-v', '--verbose', type=int, choices=[0, 1, 2], help='Print Verbose Output')
parser.add_argument('--debug', action='store_true', help='Print Debugging Output')

args = parser.parse_args()

if args.debug:
    print('Debugging Output')

print(args)
print(args.greeting)
print(args.numbers)

if not args.verbose or args.verbose >= 0:
    print(f'\nThe sum of {args.numbers} is: {sum(args.numbers)}\n')
if args.verbose >= 1:
    print('More info.\n')
if args.verbose == 2:
    print('Even more info.\n')

# if args.numbers:
#     print(sum(args.numbers))