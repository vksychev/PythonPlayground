import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str)
parser.add_argument("--value", type=str)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
try:
    file = open(storage_path)
except IOError as e:
    with open(storage_path, 'w') as f:
        f.write("{}")
else: file.close()

if (args.key is not None) & (args.value is not None):

    with open(storage_path, 'r') as r:
        d2 = json.loads(r.read())
    if args.key in d2:
        s = []
        s.append(d2[args.key])
        s.append(args.value)
        d2[args.key] = s
    else:
        d2[args.key] = args.value
    with open(storage_path, 'w') as f:
        json.dump(d2, f)
        f.close()
elif args.key is not None:
    with open(storage_path, 'r') as r:
        d2 = json.loads(r.read())
    if args.key in d2:
        print(str(d2[args.key]).strip('[]'))

else:
    print('')
