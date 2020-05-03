import environ
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))


def _set_django_settings_module():
    build_stage = env("BUILD_STAGE")
    if build_stage == "PROD":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RemindMe.production")
    elif build_stage == "LOCAL":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RemindMe.local")
