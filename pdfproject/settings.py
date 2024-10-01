
import os
from pathlib import Path
from mongoengine import connect
from dotenv import load_dotenv
load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG")

# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = [".vercel.app"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "backend"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pdfproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'backend/templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pdfproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {}


MONGODB_SETTINGS = {
    'db': os.environ.get("DBNAME"),
    'host': os.environ.get("DBHOST"),
    'username': os.environ.get("DBUSERNAME"),
    'password': os.environ.get("DBPASSWORD"),
    'port': os.environ.get("DBPORT"),
    'authentication_source': 'admin',
    'use_srv': os.environ.get("DB_USE_SRV"),
    'retryWrites': True,
    'ssl': True,
}

if MONGODB_SETTINGS.get('use_srv', False):
    # For MongoDB Atlas or srv connection (use +srv)
    connection_uri = (
            f"mongodb+srv://{MONGODB_SETTINGS['username']}:"
            f"{MONGODB_SETTINGS['password']}@"
            f"{MONGODB_SETTINGS['host']}/"
            f"{MONGODB_SETTINGS['db']}?retryWrites=true&w=majority"
        )
else:
    # For direct connections (use normal mongodb://)
    connection_uri = (
        f"mongodb://{MONGODB_SETTINGS['username']}:"
        f"{MONGODB_SETTINGS['password']}@"
        f"{MONGODB_SETTINGS['host']}:{MONGODB_SETTINGS['port']}/"
        f"{MONGODB_SETTINGS['db']}"
    )

# Connect to MongoDB
connect(
    db=MONGODB_SETTINGS['db'],
    host=connection_uri,
    ssl=MONGODB_SETTINGS.get('ssl'),
    retryWrites=MONGODB_SETTINGS.get('retryWrites'),
)


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
