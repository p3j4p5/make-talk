"""Creates a skelton for and manges a LaTeX Beamer presentation."""

import argparse


DESCRIPTION = (
    "This program helps to create a LaTeX Beamer presentation structure. "
    "It can also be used to maintain a presentation structure created with it."
    )


def main():
    """Entry point for this script."""

    args = parse_args()


def parse_args():
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    subparsers = parser.add_subparsers(
        help='Commands to create and maintain LaTeX Beamer talk structure.',
        description='Available make-talk commands',
        dest='commands',
        )

    init = subparsers.add_parser(
        'init',
        help='Create a new empty LaTeX Beamer presentation'
        )

    init.add_argument(
        '-a', '--author',
        metavar="AUTHOR",
        help='Set talk author. Overrides parameter set in config file.'
        )

    init.add_argument(
        '-c', '--config',
        metavar="CONFIG",
        help='Path to config file storing parameters like author name and '
             'talk title, to set up talk. Command line parameters have '
             'precedence over config file parameters.'
        )

    init.add_argument(
        '-i', '--institute',
        metavar='INSTITUTE',
        help='Set talk institute. Overrides parameter set in config file.'
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

    args = parser.parse_args()

    if args.commands == 'init':
        if not args.date:
            args.date = '\\today'

    return args


if __name__ == '__main__':
    main()
