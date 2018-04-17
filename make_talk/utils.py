import errno
import os


def abs_path(path):
    """Return absolute path from given path string

    Expands '~' and all '$' variables, and prepends the current working
    directory in case the given path is relative.

    Args:
        path: String representing a (relative) path.

    Returns:
        String representing absolute path with all variables expanded.
    """
    if path:
        path = os.path.realpath(os.path.expandvars(os.path.expanduser(path)))

    return path


def mkdir_p(path):
    """Create directory tree

    Mimicking 'mkdir -p <path>' in the shell.

    Args:
        path: String representing the path to be created.
    """
    path = abs_path(path)
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
