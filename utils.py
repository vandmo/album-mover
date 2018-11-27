import json
import os


def writejson(filename, v):
    with open(filename, 'w') as f:
        f.write(json.dumps(v, indent=2))


def mkdirsafeish( name ):
    if not os.path.exists(name):
        os.makedirs(name)
