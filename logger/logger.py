from enum import Enum
import os
import time
from datetime import datetime

logger_config = {}
initialized = False

# convert to string from seconds
def strfseconds(seconds):
    hr = int(seconds/3600)
    min = int((seconds-hr*3600)/60)
    sec = seconds - hr*3600 - min*60
    return '{} hours {} mins {:.2f} seconds'.format(hr, min, sec)

class LogLevel(Enum):
    DEBUG = 5
    INFO = 10
    ERROR = 20
    WARNING = 15

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_log_dir():
    path = os.path.join(logger_config['log_path'], 'log')
    make_dir(path)
    path = os.path.join(path, logger_config['name'])
    make_dir(path)

    return path

def record(*args, **kwargs):
    string = datetime.now().strftime('%Y:%m:%d:%H:%M:%S') +':' 
    for arg in args:
        string += str(arg) + ' '
    for key, val in kwargs.items():
        string += str(key) + ':' + str(val)
    print(string)
    logger_config['_log_file'].write(string + '\n')


def add_record(level, *args, **kwargs):
    if level.value >= logger_config['level'].value:
        record(*args, **kwargs)

def info(*args, **kwargs):
    add_record(LogLevel.INFO, *args, **kwargs)

def debug(*args, **kwargs):
    add_record(LogLevel.DEBUG, *args, **kwargs)

def error(*args, **kwargs):
    add_record(LogLevel.ERROR, *args, **kwargs)

def warning(*args, **kwargs):
    add_record(LogLevel.WARNING, *args, **kwargs)

def init(name, level='INFO', log_path = None):
    
    global initialized


    if initialized:
        return

    initialized = True
    logger_config['name'] = name
    logger_config['level'] = LogLevel[level]
    logger_config['start'] = time.time()
    if log_path is None:
        logger_config['log_path'] = os.path.expanduser('~')
    else:
        logger_config['log_path'] = logger_config

    path = get_log_dir()
    path = os.path.join(path, datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    os.makedirs(path)
    logger_config['log_file'] = os.path.join(path, 'log.txt')
    logger_config['_log_file'] = open(logger_config['log_file'], "a")
    
    return None

def done():
    elapsed = time.time() - logger_config['start']
    record('done in ', strfseconds(elapsed))
    logger_config['_log_file'].close()


if __name__ == "__main__":
    init('log_test')
    info('add info')
    warning('add error', 'add error')
    debug('dont add this')
    error(name = 'keyword test')
    done()