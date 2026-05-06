from config.env import env_bool, env_list

from .base import *  # noqa: F401,F403


DEBUG = env_bool("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS", default=[])
