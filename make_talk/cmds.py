from distutils import dir_util
import os.path

from make_talk.utils import abs_path


def init(args):
    # TODO: docstring

    talk_dir = os.path.join(abs_path(args.directory), '.talk')

    dir_util.mkpath(talk_dir)

    # copy latex files boom!
    #dir_util.copy_tree()
