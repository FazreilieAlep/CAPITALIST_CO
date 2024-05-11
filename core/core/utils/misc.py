import yaml

# pass string dict to proper python
# dockerfile doesnt take python syntax. Need to stringify to give data to docker
def yaml_coerce(value):
    # convert value to proper Python

    if isinstance(value, str):
        # yaml.load returns a Python object (we are just creating some quick yaml data with a dummy)
        # Converts string dict "{'apples':1, 'bacon': 2}" to Python dict
        # Useful because sometimes we need to stringify settings this way (like in Dockerfile)
        return yaml.load(f'dummy : {value}', loader=yaml.SafeLoader)['dummy']
    
    return value