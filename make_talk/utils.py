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
