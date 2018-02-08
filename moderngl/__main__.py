'''
    ModernGL main
'''

import argparse
import json
import os
import sys

import moderngl


def main(argv=None):
    '''
        main
    '''

    parser = argparse.ArgumentParser(prog='moderngl')
    parser.add_argument('-v', '--version', action='version', version='moderngl %s' % moderngl.__version__)
    parser.add_argument('-i', '--info', action='store_true', default=False)
    args = parser.parse_args(argv)

    ctx = moderngl.create_standalone_context()

    if args.info:
        print(json.dumps(ctx.info, sort_keys=True, indent=4))

    else:
        repo = os.path.isfile(os.path.join(os.path.dirname(__file__), 'README.md'))
        install = '(git repository)' if repo else '(installed)'

        print('moderngl:', moderngl.__version__, install)
        print('Vendor:', ctx.info['GL_VENDOR'])
        print('Renderer:', ctx.info['GL_RENDERER'])
        print('Version:', ctx.info['GL_VERSION'])
        print('Python:', sys.version)
        print('Platform:', sys.platform)


if __name__ == '__main__':
    main()
