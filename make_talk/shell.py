"""Creates a skelton for and manges a LaTeX Beamer presentation."""

import argparse

import make_talk
from make_talk import cmds


DESCRIPTION = (
    "This program helps to create a LaTeX Beamer presentation structure. "
    "It can also be used to maintain a presentation structure created with it."
    )


def main():
    """Entry point for this script."""

    args = parse_args()

    if args.command == 'init':
        cmds.init(args)


def parse_args():
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--version',
                        action='version',
                        version=make_talk.__version__)

    subparsers = parser.add_subparsers(
        help='Commands to create and maintain LaTeX Beamer talk structure.',
        description='Available make-talk commands',
        # Using uncodumented argument 'dest' storing the selected subparser,
        # i.e. command.
        dest='command',
        )

    init = subparsers.add_parser(
        'init',
        # TODO: Reinitialise?
        help='Create an empty LaTeX Beamer presentation'
        )

    init.add_argument(
        'directory',
        metavar='DIRECTORY',
        nargs='?',
        default='./',
        help='Set target directory for LaTeX Beamer presentation. '
             '(default = %(default)s)'
        )

    init.add_argument(
        '-a', '--author',
        metavar='AUTHOR',
        help='Set talk author. Overrides parameter set in config file.'
        )

    init.add_argument(
        '-b', '--no-backup',
        action='store_true',
        default=False,
        help='Do not create backup slides. '
             'Overrides parameter set in config file. (default = %(default)s)'
        )

    init.add_argument(
        '-d', '--date',
        metavar='DATE',
        help="Set talk date. Overrides parameter set in config file. "
             "(default = Latex's \\today)"
        )

    init.add_argument(
        '-i', '--institute',
        metavar='INSTITUTE',
        help='Set talk institute. Overrides parameter set in config file.'
        )

    init.add_argument(
        '-o', '--no-outline',
        action='store_true',
        default=False,
        help='Do not create outline slides (only relevant if TOC is created). '
             'Overrides parameter set in config file. (default = %(default)s)'
        )

    init.add_argument(
        '-s', '--short-author',
        metavar='SHORT',
        help="Set the talk's short author field. "
             "Overrides parameter set in config file. (default = AUTHOR)"
        )

    init.add_argument(
        '-t', '--title',
        help='Set title talk. Overrides parameter set in config file.'
        )

    init.add_argument(
        '-T', '--no-toc',
        default=False,
        help='Do not create table of content and outline slides. '
             'Overrides parameter set in config file. (default = %(default)s)'
        )

    args = parser.parse_args()

    if args.command == 'init':
        if not args.date:
            args.date = '\\today'

    return args


if __name__ == '__main__':
    main()
