# import sys

# if len(sys.argv) > 1:
#   name = sys.argv[1]
#   print("Hello " + name)
# else:
#   print("No name provided!")


import argparse

parser = argparse.ArgumentParser(description="This is my dog roger")

parser.add_argument('-c','--color',metavar='color',required=True,choices={"red","yellow"},help='The color to search for')

args = parser.parse_args()

print(args.color)