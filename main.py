import sys
import src.parser as parser

import yaml

def test():
  print(sys.argv[1])

def main():
  parser.yaml_read(sys.argv[1])

if __name__ == '__main__':
  main()
