import sys
import nose

def run(argv=[]):
    return nose.run(argv=[
            '-i ^(it|ensure|must|should|deve|specs?|examples?)',
            '-i (specs?|examples?|exemplos?)(.py)?$',
            '--with-spec',
            '--spec-color',
            ] + argv)

def main():
    sys.exit(run(sys.argv[1:]))
