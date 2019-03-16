# storage of dictionary key-value in temporary file
import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
if args.key:
    key_name = args.key

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.isfile(storage_path):
    with open(storage_path, 'w') as f:
        pass
with open(storage_path, 'r') as f:
    json_dict = f.read()
    if json_dict:
        storage_dict = json.JSONDecoder().decode(json_dict)
    else:
        storage_dict = {}
if args.val:  # storing data
    key_value = args.val
    # update dictionary
    if key_name in storage_dict:
        storage_dict[key_name] += [key_value]
    else:
        storage_dict[key_name] = [key_value]
    # write dictionary to file
    with open(storage_path, 'w') as f:
        f.write(json.JSONEncoder().encode(storage_dict))
else:  # read data
    if key_name in storage_dict:
        print(', '.join(storage_dict[key_name]))
    else:
        print('')

""" #Tutors code
import argparse
import json
import os
import tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def clear():
    os.remove(storage_path)


def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        clear()
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')
"""
