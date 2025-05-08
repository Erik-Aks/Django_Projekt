SECRET_KEY = "psst"  # В продакшене используйте защищенный ключ!
DEBUG = True  # Установите False в продакшене

# Основные настройки Django
USE_I18N = False
USE_TZ = True

# Настройки приложений
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.humanize",

    # Allauth и зависимости
    "allauth",
    "allauth.account",
    "allauth.mfa",
    "allauth.socialaccount",



    # OTP аутентификация
    "otp",
    "otp_totp",
]

# Промежуточное ПО
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# Настройки аутентификации
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Настройки сайта
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# Настройки Allauth
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # или 'none' если не нужна верификация
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
ACCOUNT_SIGNUP_FIELDS = ['email']  # Обязательное поле email

# Настройки MFA
MFA_ENABLED = True  # Включить многофакторную аутентификацию
MFA_TOTP_ENABLED = True  # Включить TOTP (Google Authenticator)
MFA_PASSKEY_ENABLED = False  # Отключить Passkeys если не нужны
MFA_RECOVERY_CODE_ENABLED = True  # Включить коды восстановления

# Настройки модели
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Отключение системных проверок (только для разработки!)
SILENCED_SYSTEM_CHECKS = [
    'models.W042',  # Предупреждения OpenID
]
# Konfiguracja OpenID
SOCIALACCOUNT_PROVIDERS = {
    'openid': {
        'SERVERS': [
            # Lista serwerów OpenID (np. Google, Yahoo)
            {'id': 'google', 'name': 'Google', 'openid_url': 'https://www.google.com/accounts/o8/id'},
        ]
    }
}

# Rozwiązanie problemu z kluczami
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SILENCED_SYSTEM_CHECKS = ['models.W042']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
TWILIO_ACCOUNT_SID = 'your_sid'
TWILIO_AUTH_TOKEN = 'your_token'
TWILIO_PHONE_NUMBER = '+1234567890'
