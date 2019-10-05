# argparser generate error with hydrogen.
# to avoid the error, excute the follows first:
import sys
sys.argv=['']
del sys
# ----------------------

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--age", type=int, default=16, help="your age.")
parser.add_argument("--name", type=str, default=None, help="your name.")
args = parser.parse_args()

print("your age is ", args.age)
print("your name is ", args.name)

args.name='abc'
print("your name is %s and your age is %d" %(args.name,args.age))
