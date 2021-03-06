# This file is part of Buildbot.  Buildbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Buildbot Team Members

import os


def isBuildslaveDir(dir):
    def print_error(error_message):
        print "%s\ninvalid buildslave directory '%s'" % (error_message, dir)

    buildbot_tac = os.path.join(dir, "buildbot.tac")
    try:
        contents = open(buildbot_tac).read()
    except IOError, exception:
        print_error("error reading '%s': %s" %
                    (buildbot_tac, exception.strerror))
        return False

    if "Application('buildslave')" not in contents:
        print_error("unexpected content in '%s'" % buildbot_tac)
        return False

    return True
