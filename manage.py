#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "legra_site.settings.dev")


    if os.path.isfile(os.path.join(os.path.dirname(__file__), 'local_settings.py')):
        # Если рядом с manage.py лежит local_settings.py — используем его
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings")
    else:
        # Если нет — используем стандартные настройки без секретов
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "legra_site.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)