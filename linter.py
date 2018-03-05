#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Gregory Oschwald (based on linter by Aparajita Fishman)
# Copyright (c) 2013 Gregory Oschwald, Aparajita Fishman
#
# License: MIT
#

"""This module exports the PerlCritic linter class."""

import os
from SublimeLinter.lint import Linter, util


class PerlCritic(Linter):

    """Provides an interface to perlcritic."""

    syntax = ('modernperl', 'perl')
    regex = r'\[.+\] (?P<message>.+?) at line (?P<line>\d+), column (?P<col>\d+).+?'
    cmd = [ 'perlcritic', '--verbose', '8']
