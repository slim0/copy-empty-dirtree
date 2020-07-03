#!/usr/bin/env python
# coding: utf8

import os
import sys

if len(sys.argv) != 3:
    print("Please specify, as the first argument, the source folder and as the second argument the destination folder.")
    sys.exit(1)

SRC = sys.argv[1]
DEST = sys.argv[2]


def create_empty_dirtree(srcdir, dstdir, onerror=None):
    """
    Allows you to duplicate a tree folder (without the files, only folders).
    :param srcdir: The source directory you want to duplicate. If it ends with a 'os.path.sep', function will not
    duplicate the root folder.
    :param dstdir: The destination where you want to have your fresh new tree folder.
    :param onerror:
    """
    dstdir = os.path.abspath(dstdir)
    if not srcdir[-1] == os.path.sep:
        dstdir += os.path.sep + srcdir.split(os.path.sep)[-1]
    srcdir = os.path.abspath(srcdir)
    srcdir_prefix = len(srcdir) + len(os.path.sep)
    if not os.path.exists(dstdir):
        os.makedirs(dstdir)
    for root, dirs, files in os.walk(srcdir, onerror=onerror):
        for dirname in dirs:
            dirpath = os.path.join(dstdir, root[srcdir_prefix:], dirname)
            try:
                if not os.path.exists(dirpath):
                    os.mkdir(dirpath)
            except OSError as error:
                if onerror is not None:
                    onerror(error)


if __name__ == '__main__':
    create_empty_dirtree(SRC, DEST)
    print("DONE")
