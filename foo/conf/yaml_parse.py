import yaml


def get_config(path):
    f = open(path, encoding='utf8')
    data = f.read()
    f.close()
    yaml_reader = yaml.load(data, yaml.FullLoader)
    return yaml_reader
