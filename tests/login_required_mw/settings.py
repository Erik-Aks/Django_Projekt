from pathlib import Path
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Импортируем INSTALLED_SOCIALACCOUNT_APPS из общего файла
try:
    from tests.common.settings import INSTALLED_SOCIALACCOUNT_APPS
except ImportError:
    INSTALLED_SOCIALACCOUNT_APPS = ()  # Если не удалось импортировать, установим пустой список

# Секретный ключ (не использовать в продакшене)
SECRET_KEY = "psst"

# Настройки сайта
SITE_ID = 1

# Разрешенные хосты
ALLOWED_HOSTS = (
    "testserver",
    "example.com",
)

USE_I18N = False
USE_TZ = True

# Настройки базы данных (SQLite in-memory - для тестов)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

# Настройки URL-ов
ROOT_URLCONF = "tests.login_required_mw.urls"  # Корневой URL-конфиг
LOGIN_URL = "/accounts/login/"  # URL для перенаправления на страницу входа

# Шаблоны
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

# Кэш (по умолчанию DummyCache для тестов)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Middleware
MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Добавьте вашу кастомную middleware (проверьте, что файл настроен верно)
    "django.contrib.auth.middleware.LoginRequiredMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
)

# Установленные приложения (INSTALLED_APPS)
INSTALLED_APPS = (
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
                     "allauth.headless",
                 ) + INSTALLED_SOCIALACCOUNT_APPS

# Бэкенды аутентификации
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Настройки статических файлов
STATIC_ROOT = "/tmp/"  # Для тестов
STATIC_URL = "/static/"


# Кастомный хэшер паролей (для тестов, не используйте в продакшене)
class MyPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    """
    Кастомный хэшер паролей, использующий 1 итерацию.
    Используется только для тестов. Не применять на продакшене!
    """
    iterations = 1


# Настройки хэша паролей
PASSWORD_HASHERS = [
    "tests.login_required_mw.settings.MyPBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Настройки социальных приложений
SOCIALACCOUNT_QUERY_EMAIL = True
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

# Поддержка входа по коду
ACCOUNT_LOGIN_BY_CODE_ENABLED = True

# Кастомный адаптер аккаунтов (проверьте правильность пути к адаптеру)
ACCOUNT_ADAPTER = "tests.common.adapters.AccountAdapter"

# Настройки многофакторной аутентификации
MFA_SUPPORTED_TYPES = ["totp", "webauthn", "recovery_codes"]
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_PASSKEY_SIGNUP_ENABLED = True

# Поддержка Headless режима
HEADLESS_SERVE_SPECIFICATION = True
