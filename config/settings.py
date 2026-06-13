import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Keep secret key in env var for production
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

# DEBUG must be False in production (set via env var)
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]  # Restrict this in real production

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# SQLite for simplicity — swap for Postgres in real CI/CD
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Logging config: ensures our log pattern goes to console (good for Docker/K8s log collection) ---
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}