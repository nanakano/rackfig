import yaml

def yaml_read(input_yaml):
  with open(input_yaml) as file:
    obj = yaml.safe_load(file)
  print(obj)

