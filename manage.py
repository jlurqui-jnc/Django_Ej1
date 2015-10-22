#!/usr/bin/env python
import os
import sys
#import site

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djEj1.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#path = lambda *a: os.path(...)
#site.addsitedir(path('apps'))