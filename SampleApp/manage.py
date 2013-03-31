#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


def main():
    ## We need a main() to use as entry point
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SampleApp.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
