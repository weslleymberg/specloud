import sys
import subprocess

def run():
    return subprocess.call(['nosetests',
            '-i',
            '^(it|ensure|must|should|deve|specs?|examples?)',
            '-i',
            '(specs?|examples?|exemplos?)(.py)?$',
            '--with-spec',
            '--spec-color',
            ] + sys.argv[1:])

def main():
    sys.exit(run())
