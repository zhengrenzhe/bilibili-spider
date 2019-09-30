from yaml import load, Loader


def read_yaml(path: str):
    file_data = open(path).read()
    yaml_data = load(file_data, Loader=Loader)
    return yaml_data
