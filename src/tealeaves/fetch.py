# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2025 Jani Nikula <jani@nikula.org>

import argparse
import re
import subprocess

# We could clone the repo, but save some bandwidth by retrieving the latest tag
# via git ls-remote, and its date via git web interface.

GIT_URL='git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git'
WEB_URL='https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tag'

def get_latest_tag():
    args = ['git', '-c', 'versionsort.suffix=-', 'ls-remote', '--exit-code',
            '--refs', '--sort=version:refname', '--tags', GIT_URL, '*.*']

    result = subprocess.run(args, capture_output=True, text=True, check=True)
    result = result.stdout.splitlines()[-1]
    result = result.split('/')[-1]

    return result

def get_tag_date(tag):
    # curl handles anubis
    args = ['curl', '--silent', f'{WEB_URL}/?h={tag}']

    result = subprocess.run(args, capture_output=True, text=True, check=True)
    result = result.stdout

    mo = re.search(r'<td>tag date</td>\s*<td>(.*?)</td>', result)
    if not mo:
        return None

    return mo.group(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['tag', 'date'])
    parser.add_argument('--tag')
    args = parser.parse_args()

    if args.mode == 'tag':
        print(get_latest_tag())
    elif args.mode == 'date':
        tag = args.tag if args.tag else get_latest_tag()
        print(get_tag_date(tag))

if __name__ == '__main__':
    main()
