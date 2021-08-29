#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from adminpage import loader
from ai_api.utils import download_model


def main():
    """Run administrative tasks."""
    # if sys.argv:
    #     if len(sys.argv) >= 1:
    #         if sys.argv[1] == 'runserver':
    #             loader.model = download_model()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adminpage.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
