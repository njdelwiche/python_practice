import argparse
import sys

# Practicing different python features

# join for concatenating more than 2 strings
names = ['Bob', 'Joe', 'Sally', 'Tom']
combined = ' and '.join(names)
#print(combined)

# command line interfaces with argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=10.0, 
                        help="What is the first number")
    parser.add_argument('--y', type=float, default=10.0, 
                        help="What is the second number")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    return args.x + args.y

# if __name__ == '__main__':
#     main()

# Generator expression
generate_numbers = (x for x in range(100))
print(generate_numbers) 