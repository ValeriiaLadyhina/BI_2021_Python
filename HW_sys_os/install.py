#!/usr/bin/env python3
import os

def installation():
    path = str(os.get_exec_path()[0])
    print(path)
    scripts = ['cat.py', 'ls.py', 'mkdir.py', 'rm.py', 'sort.py', 'wc.py']
    for script in scripts:
        script_path = os.path.join(path, script)
        os.chmod(script_path, 0o0777)


if __name__ == '__main__':
    installation()
