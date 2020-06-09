#!/usr/bin/env python3
# minimal example

import argparse

print("The python test runner was called")
parser = argparse.ArgumentParser(description='See documentation of cargo test runner for custom test framework')
parser.add_argument('runner_args', type=str, nargs='*')
args = parser.parse_args()
print("Arguments: {}".format(args.runner_args))
# Something like calling the test executable would happen here then
