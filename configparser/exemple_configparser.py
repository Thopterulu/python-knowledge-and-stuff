import configparser

# we create the config object
config = configparser.ConfigParser()

# we load the informations of the file
config.read('my-config.ini')

# we display hello value
print(config['DEFAULT']['Hello'])

# every category works like a python dictionnary

# with sections() you can display every category except DEFAULT
# because DEFAULT is a special word for config parser it's all in the name :)
print(config.sections())
