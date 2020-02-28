from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'debug': 'true',
    'secret_key': 'abc123',
    'long_path': '/my_app/log'
}

config['db'] = {
    'db_name': 'myapp_new',
    'db_host': 'localhost',
    'db_port': '3699'
}

config['files'] = {
    'use_cdn': 'false',
    'path': 'my_app/images'
}

with open('dev.ini', 'w') as f:
    config.write(f)

config.read('dev.ini')
print(config.sections())
print(config.get('settings', 'secret_key'))
print(config.options('settings'))


print('db' in config)

print(config.getint('db', 'db_port'))

#print(config.getint('db', 'db_port'), fallback=1234)