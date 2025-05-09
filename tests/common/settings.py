from typing import Tuple
from pathlib import Path
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Basic Django Settings
SECRET_KEY = "psst"
SITE_ID = 1
ALLOWED_HOSTS = ["testserver", "example.com"]
USE_I18N = False
USE_TZ = True
ROOT_URLCONF = "tests.regular.urls"
LOGIN_URL = "/accounts/login/"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path(__file__).parent / "templates"],
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

# Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Middleware
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# Social Account Providers
INSTALLED_SOCIALACCOUNT_APPS: Tuple[str, ...] = (
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.linkedin_oauth2",
    "allauth.socialaccount.providers.microsoft",
    "allauth.socialaccount.providers.apple",
    "allauth.socialaccount.providers.twitter_oauth2",
)

# Try to add SAML if available
try:
    import onelogin  # noqa

    INSTALLED_SOCIALACCOUNT_APPS += ("allauth.socialaccount.providers.saml",)
except ImportError:
    pass

# Installed Apps
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.humanize",
    "allauth",
    "allauth.account",
    "allauth.mfa",
    *INSTALLED_SOCIALACCOUNT_APPS,
]

# Authentication
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


# Password Hashers (testing purpose only — not for production)
class MyPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    iterations = 1


PASSWORD_HASHERS = [
    "tests.regular.settings.MyPBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Allauth Settings
ACCOUNT_SIGNUP_FIELDS = ['email']  # Указывается только email для регистрации
ACCOUNT_LOGIN_METHODS = 'email'  # Логин строго через email
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Обязательная проверка email

# Если логин по username также требуется, используйте:
# ACCOUNT_SIGNUP_FIELDS = ['username', 'email']
# ACCOUNT_LOGIN_METHODS = 'username_email'

# Социальные сети
SOCIALACCOUNT_QUERY_EMAIL = True  # Обязательное получение email для социальных аккаунтов
SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        "APPS": [
            {
                "provider_id": "unittest-server",
                "name": "Unittest Server",
                "client_id": "Unittest client_id",
                "client_secret": "Unittest client_secret",
                "settings": {
                    "server_url": "https://unittest.example.com",
                },
            },
            {
                "provider_id": "other-server",
                "name": "Other Example Server",
                "client_id": "other client_id",
                "client_secret": "other client_secret",
                "settings": {
                    "server_url": "https://other.example.com",
                },
            },
        ],
    }
}

# MFA Settings
MFA_SUPPORTED_TYPES = ["totp", "webauthn", "recovery_codes"]
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_PASSKEY_SIGNUP_ENABLED = False  # Избежание конфликта с верификацией email

# Headless Mode
HEADLESS_SERVE_SPECIFICATION = True

# Static Files
STATIC_ROOT = "/tmp/"
STATIC_URL = "/static/"
