import dj_database_url

from .local import *

ALLOWED_HOSTS += ["remind-me-backend.herokuapp.com"]

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES["default"].update(db_from_env)
