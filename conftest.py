import os
import sys

import django

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")

django.setup()
