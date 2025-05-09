import nox

DJANGO_PYTHON_REQ = {
    "4.2.20": ("3.8", "3.9", "3.10", "3.11"),
    "5.0": ("3.10", "3.11", "3.12"),
    "5.1": ("3.10", "3.11", "3.12"),
    "5.2": ("3.10", "3.11", "3.12", "3.13"),
}
DJANGO_LTS = "5.2"


@nox.session
def docs(session):
    session.install(
        "Django>=4.2,<6",
        "Sphinx>=7.4.7,<8",
        "sphinx_rtd_theme",
        "djangorestframework>=3.15.2,<4",
        "django-ninja>=1.3.0,<2",
        "snowballstemmer<3",
    )
    session.run("sphinx-build", "docs/source", "docs/build")  # Исправлено


@nox.session(tags=["lint"])
def lint(session):
    session.install("bandit")
    session.run("bandit", "-c", "pyproject.toml", "-r", "allauth/")


@nox.session(tags=["lint"])
def isort(session):
    session.install("isort==5.13.2")
    session.run("isort", "--check-only", "--diff", ".")


@nox.session(tags=["lint"])
def flake8(session):
    session.install("flake8==7.3.0")  # Совместимая версия
    session.run("flake8", "allauth/")


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"])
@nox.parametrize("django", list(DJANGO_PYTHON_REQ.keys()))
def test(session, django):
    supported_python = DJANGO_PYTHON_REQ.get(django, [])
    if session.python not in supported_python:
        session.skip(f"Django {django} не поддерживается для Python {session.python}")

    session.install(f"django=={django}")
    session.install("-r", "requirements/base.txt")
    session.run(
        "pytest",
        "--ds=tests.regular.settings",
        "allauth/",
    )
