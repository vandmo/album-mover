import json
import os


def readjson(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())


def writejson(filename, v):
    with open(filename, 'w') as f:
        f.write(json.dumps(v, indent=2))


def mkdirsafeish(name):
    if not os.path.exists(name):
        os.makedirs(name)

def file_contains(path, content):
    with open(path) as f:
        return content in f.read()
