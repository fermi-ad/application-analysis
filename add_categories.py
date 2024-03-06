#!/usr/bin/env python3

import argparse
import json
import signal

from pick import pick


def signal_handler(sig, frame):
    print(f'\nWriting changes to file...')
    write_json(data)
    print('Exiting...')
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser(description='Add tags to JSON objects.')
parser.add_argument('file', type=str, help='The JSON file to add fields to.')
parser.add_argument('-d', '--debug', action='store_true', help='Print debug messages.')
args = parser.parse_args()

def read_json(filename=args.file):
    with open(filename, 'r') as file:
        return json.load(file)

def write_json(data, filename=args.file):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def main(data):
    domain_tags = set()
    ad_group_options = [
        'a0',
        'bnb',
        'boone',
        'booster',
        'cdf',
        'controls',
        'cryo',
        'cwctf',
        'd0',
        'ecool',
        'ee',
        'extbeams',
        'general',
        'holometer',
        'inst',
        'interlocks',
        'linac',
        'mech',
        'mi/rr',
        'mr',
        'mta',
        'muon',
        'nova',
        'numi',
        'ops',
        'pbar',
        'rf',
        'sy',
        'target',
        'tev',
    ]

    for index, obj in enumerate(data):
        if 'ad_group' in obj or 'domain' in obj:
            if 'domain' in obj:
                domain_tags.update(obj['domain'])

            continue

        print(f"{index + 1} of {len(data)} programs")
        print(f"Program: {obj['program']}")
        print(f"Description: {obj['description']}")
        print(f"Type: {obj['type']}")
        print(f"Keeper: {obj['keeper']}")
        print(f"Index Page: {obj['index_page']}")
        print(f"Execution Count: {obj['execution_count']}")

        input("Press any key to continue...")

        ad_group = pick(sorted(ad_group_options), title='Select ad_group', multiselect=True)
        obj['ad_group'] = [item[0] for item in ad_group]

        if domain_tags:
            domain = pick(sorted(domain_tags), title='Select domain', multiselect=True)
            domain_items = [item[0] for item in domain]
            obj['domain'] = domain_items
            domain_tags.update(domain_items)

        new_domains = input("Enter domain (space-separated): ").split()

        if 'domain' in obj:
            obj['domain'] = obj['domain'] + new_domains
        else:
            obj['domain'] = new_domains

        domain_tags.update(new_domains)

        print("------------------------------------------------------------------")
        print(f"AD Groups: {obj['ad_group']}")
        print(f"Domains: {obj['domain']}")
        print("------------------------------------------------------------------")

    write_json(data)

if __name__ == '__main__':
    data = read_json()
    main(data)
